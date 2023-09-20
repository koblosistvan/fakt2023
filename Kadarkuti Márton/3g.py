import random


adat = dict(kő = "olló", papír ="kő", olló = "papír") # nyer = "veszt"

player = ""

while player not in adat:
    player = str(input("> "))


#Ennek kéne nyernie: adat.get(player)


print(f"\nTe: [{player}]")

c = ["kő", "papír", "olló"]

com = c[random.randint(0,2)]

print(f"Program: [{com}]" )
print("--------------------")

#Döntetlen
if player == com:
    print("Döntetlen.")
    quit()

#Nyert
if adat.get(player) == com:
    print("Nyertél.")
    quit()

#Vesztett
print("Vesztettél.")