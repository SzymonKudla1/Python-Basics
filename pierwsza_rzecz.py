print("Hello world!")

imie = input("Jak masz na imię? ")

#print('Hello', imie)

if imie != "Szymon":
    print("Nie znam cię!")
else:
    print("Witaj ponownie!")

wiek = int(input("Ile masz lat? "))

if wiek < 18:
    print("Nie jesteś pełnoletni")
    print("Brakuje ci", 18 - wiek, "lat.")
else:
    print("Jesteś pełnoletni")
