from random import choice

point = 1, 2

print(point[0])
print(point[1])

cities = ["Gdynia", "Gdańsk", "Sopot"]
print(cities[0])
print(cities[-1])
print(cities)

cities.append("Kraków")
cities.append("Warszawa")
cities.append("Wrocław")

print(cities)

cities.sort()
print(cities)

capitals = {
    "Poland": "Warszawa",
    "France": "Paris",
    "Germany": "Barlin"
}

print(capitals["Poland"])

losowe_panstwo = choice(list(capitals.keys()))

capital = input(f"Jaka jest stolica {losowe_panstwo}? ")
if capitals[losowe_panstwo] == capital:
    print("Bardzo dobrze")
else:
    print("Zła odpowiedz, chodziło o", capitals[losowe_panstwo])

    