# def say_hello():
#     print("Hello")

# say_hello()
# say_hello()


# def say_your_name(first_name=""):
#     print(f"Hello {first_name}")

# say_your_name("Adam")
# say_your_name("Damian")
# say_your_name("Ela")
# say_your_name()

def calculate_brutto(netto, vat=0.23):
    return netto + netto * vat

total = calculate_brutto(100)
total += calculate_brutto(200)

print(total)

