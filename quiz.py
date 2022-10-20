print("Witaj w grze!")
print("Wybierz jedną odpowiedź wpisując A, B C lub D")

points = 0

print("1. Ile nóg ma koń? A-1, B-2, C-3, D-4")
odpowiedz_1 = input("")
if odpowiedz_1 == "D":
    print("Brawo, dobra odpowiedź!")
    points += 1
else:
    print("Źle! Poprawna odpowiedź to D-4.")

print("2. Ile części ma trylogia? A-1, B-2, C-3, D-4")
odpowiedz_2 = input("")
if odpowiedz_2 == "C":
    print("Brawo, dobra odpowiedź!")
    points += 1
else:
    print("Źle! Poprawna odpowiedź to C-3.")

print(f"Zdobyłeś {points} punktów!")

