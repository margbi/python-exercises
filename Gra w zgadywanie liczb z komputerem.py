#Importowanie modułu random
import random

#Powitanie i wyjaśnienie zasad gry
print("Witaj w grze LOSOWANIE LICZB.")
print("Wybierz dowolną liczbę w zakresie od 1 do 100, a ja spróbuję ją odgadnąć!")
print("Jeśli zgadnę, wpisz GRATULACJE. Jeśli podam za małą liczbę, wpisz ZA MALA. Jeśli za dużą, wpisz ZA DUZA.")
print("\n\nZaczynamy!")

#Definiowanie zmiennych
zakres_d = 1
zakres_g = 10

#Losowanie liczby przez komputer
while True:
    liczba = random.randint(zakres_d, zakres_g)
    print("Czy ta liczba to", liczba, "?")
    odpowiedz = (input("Podpowiem Ci, że... ")).lower()
    if odpowiedz == "gratulacje":
        print("Super! Fajnie się z Tobą grało.")
        break
    if odpowiedz != "za mala" and odpowiedz != "za duza" and odpowiedz != "gratulacje":
        print("Nie grasz zgodnie z zasadami gry!")
    if odpowiedz == "za mala":
        zakres_d = liczba + 1
    if odpowiedz == "za duza":
        zakres_g = liczba - 1
    if zakres_d > zakres_g:
        print("Oszukujesz!")
        break
    
#Zakończenie programu
print("\n\nAby zakończyć program, naciśnij enter.")
