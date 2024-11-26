from binance.client import Client
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Input your Binance API credentials here
api_key = input("Enter Binance API Key: ")
api_secret = input("Enter Binance API Secret: ")

# Create the Binance client
client = Client(api_key, api_secret)

# Function to fetch historical data
def fetch_historical_data(symbol, interval='1h', limit=500):
    try:
        klines = client.get_historical_klines(symbol, interval, limit=limit)
        # Format data into DataFrame
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                           'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_vol',
                                           'taker_buy_quote_asset_vol', 'ignore'])
        # Ensure that the 'close' column is a float and 'timestamp' is a datetime
        df['close'] = df['close'].astype(float)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df[['timestamp', 'close']]
    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return pd.DataFrame()

# Function to get the lot size filter for the symbol
def get_lot_size(symbol):
    exchange_info = client.get_exchange_info()
    for symbol_info in exchange_info['symbols']:
        if symbol_info['symbol'] == symbol:
            for filter in symbol_info['filters']:
                if filter['filterType'] == 'LOT_SIZE':
                    return filter
    return None

# Function to round the quantity according to the LOT_SIZE filter
def round_quantity(symbol, quantity):
    lot_size = get_lot_size(symbol)
    if lot_size:
        step_size = float(lot_size['stepSize'])
        return round(quantity / step_size) * step_size  # Round to nearest valid step size
    return quantity

# Train a simple AI model to predict the price
def train_predict_price(symbol):
    df = fetch_historical_data(symbol)

    if df.empty:
        print("No historical data available to train the model.")
        return

    # Prepare data for training
    df['timestamp'] = df['timestamp'].apply(lambda x: x.timestamp())  # Convert datetime to UNIX timestamp (float)
    X = np.array(df['timestamp']).reshape(-1, 1)
    y = np.array(df['close'])

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next price (1 hour later)
    future_timestamp = pd.to_datetime('now') + pd.Timedelta(hours=1)  # Get current time and add 1 hour
    future_timestamp_numeric = np.array(future_timestamp.timestamp()).reshape(-1, 1)  # Convert to UNIX timestamp
    predicted_price = model.predict(future_timestamp_numeric)
    print(f"Predicted price for next hour: {predicted_price[0]}")

# Function to display available cryptos in the wallet
def view_wallet():
    account_info = client.get_account()
    balances = account_info['balances']
    available_balances = {balance['asset']: balance['free'] for balance in balances if float(balance['free']) > 0}
    return available_balances

# View available cryptos
def display_wallet_balances():
    print("Available Cryptos in Wallet:")
    available_balances = view_wallet()
    for crypto, balance in available_balances.items():
        print(f"{crypto}: {balance} available")

# Grid Trading function
def grid_trading(symbol, usdc_amount, grid_size=0.01, quantity=0.001):
    # Get current price of the symbol
    ticker = client.get_symbol_ticker(symbol=symbol)
    current_price = float(ticker['price'])
    print(f"Current price of {symbol}: {current_price} USDC")

    # Set up buy and sell orders for grid
    for i in range(1, 6):
        buy_price = current_price * (1 - grid_size * i)
        sell_price = current_price * (1 + grid_size * i)

        # Define buy and sell quantities (adjust depending on USDC amount)
        buy_quantity = usdc_amount / buy_price
        sell_quantity = usdc_amount / sell_price

        # Round quantities to conform with the LOT_SIZE filter
        buy_quantity = round_quantity(symbol, buy_quantity)
        sell_quantity = round_quantity(symbol, sell_quantity)

        # Place limit buy and sell orders
        try:
            client.order_limit_buy(symbol=symbol, quantity=round(buy_quantity, 3), price=str(round(buy_price, 2)))
            client.order_limit_sell(symbol=symbol, quantity=round(sell_quantity, 3), price=str(round(sell_price, 2)))
            print(f"Placed buy order at {buy_price} and sell order at {sell_price}")
        except Exception as e:
            print(f"Error placing orders: {e}")

# Main function to run the bot
def main():
    print("Welcome to the Binance Trading Bot")

    # Step 1: View available wallet cryptos
    display_wallet_balances()

    # Step 2: Choose a pair to trade and input trade details (must be a crypto/USDC pair)
    symbol = input("Enter the trading pair (e.g., DOGEUSDC): ")
    usdc_amount = float(input("Enter the USDC amount to trade: "))

    # Step 3: Run Grid Trading Bot
    grid_trading(symbol, usdc_amount)

    # Step 4: Predict future price using AI (optional)
    ai_prediction = input("Would you like to predict the future price using AI? (y/n): ")
    if ai_prediction.lower() == 'y':
        train_predict_price(symbol)

# Run the bot
if __name__ == "__main__":
    main()
