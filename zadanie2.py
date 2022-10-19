capitals = {"Warsaw", "London", "Paris"}
# W zbiorse wartości nie mogą się powtarzać
capitals1 = set(["Warsaw", "London", "Paris"])

# pętle

for n in range(10):
    print(n)

for _ in range(10):
    print("Wyświetlenie tekstu określoną ilość razy")


number_of_entries = 0
while number_of_entries < 30:
    entries = int(input("Ile osób wchodzi? "))
    number_of_entries += entries

    print("Aktualna ilość osób: " , number_of_entries)
