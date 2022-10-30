def instrukcja():

    print("Instrukcja obsługi To-Do List:")
    print("Wpisz 1 aby otworzyć instrukcję obsługi.")
    print("Wpisz 2 aby dadać nową pozycję do listy.")
    print("Wpisz 3 aby usunąć pozycję z listy.")
    print("Wpisz 4 aby wyświetlić całą listę.")

def dodawanie():

    pozycja_do_listy = input("Pozycja do listy: ")
    with open("ToDoList.txt", "a") as to_do_list:
        to_do_list.write(pozycja_do_listy + "\n")
        to_do_list.close()

def usuwanie():

    with open("toDoList.txt", "r") as f:
        lines = f.readlines()
    print(lines)
    linia_do_usuniecia = input("Wpisz co chcesz usunąć: ")
    with open("toDoList.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != linia_do_usuniecia:
                f.write(line)

def wyswietlanie():

    with open("toDoList.txt", "r") as f:
        caly_plik = f.read()
    print(caly_plik)
        

    
print(instrukcja())
path = "D:\Programowanie\Python\Python-Basicks\ToDoList.txt"

komenda = int(input("Wybierz liczbę odpowiadającą czynności którą chcesz wykonać: "))

if komenda == 1:
    print(instrukcja())
elif komenda == 2:
    print(dodawanie())
elif komenda == 3:
    print(usuwanie())
elif komenda == 4:
    print(wyswietlanie())


