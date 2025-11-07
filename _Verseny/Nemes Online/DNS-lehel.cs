using System;

public class DNS
{
    public static void Main(string[] args)
    {
		string be = Console.ReadLine();
		string[] adat = be.Split(new char[] { ' ' });
		bool hiba = false;
		string[] dns = new string[Convert.ToInt32(adat[0])];

		for (int i = 0; i < dns.Length; i++)
		{
			dns[i] = "?";
		}
		
		int meres = Convert.ToInt32(adat[1]);
		int[] hely = new int[meres];
		string[] kód = new string[meres];
		for (int i = 0; i <meres ; i++) 
		{ 
			be = Console.ReadLine();
			adat = be.Split(new char[] { ' ' });
			hely[i] = Convert.ToInt32(adat[0]);
			kód[i]  = adat[1];

		}
		for (int k = 0; k < meres; k++) {
			for (int i = 0; i < kód[k].Length; i++)
			{
				if (dns[hely[k] + i - 1] == "?" || dns[hely[k] + i - 1] == Convert.ToString(kód[k][i])) 
				{
					dns[hely[k] + i - 1] = Convert.ToString(kód[k][i]);
				}
				else { hiba = true; break; }

			}
		}
		string DNS = "";
		if (hiba) { Console.WriteLine("Hiba!"); }
		else { for (int i = 0; i < dns.Length; i++) { DNS += dns[i]; } Console.WriteLine(DNS); }    }
}
