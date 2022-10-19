from random import randint


randomowa_liczba = randint(1,100)

liczba = int(input("Podaj liczbę: "))

while (randomowa_liczba != liczba):
    if liczba > randomowa_liczba:
        print("Liczba jest za duża. Spróbuj ponownie.")
        liczba = int(input("Podaj liczbę: "))
    elif liczba < randomowa_liczba:
        print("Liczba jest za mała. Spróbuj ponownie.")
        liczba = int(input("Podaj liczbę: "))

print("Brawo, udało ci się zgadnąć liczbę!")






    


