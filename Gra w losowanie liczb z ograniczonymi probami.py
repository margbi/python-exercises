#Importowanie modułu random
import random

#Powitanie
print("Witaj w grze LOSOWANIE LICZB. Twoim zadaniem jest odgadnąć liczbę, którą wybiorę.")
print("Masz do wykorzystania tylko 5 prób!")

#Losowanie liczby
print("\nLiczba została wylosowana.")
the_number = random.randint(1, 10)

#Zgadywanie
guess = int(input("Zgaduję, że ta liczba to... "))
tries = 1

#Pętla zgadywania
if guess == the_number:
        print("Gratulacje, udało Ci się zgadnąć za", tries, "razem!")
while guess != the_number:
    if guess > the_number:
        print("Za duża.")
    else:
        print("Za mała.")
    guess = int(input("Ta liczba to... "))
    tries += 1
    if guess == the_number:
        print("Gratulacje, udało Ci się wygrać za", tries, "razem!")
        break
    if tries < 5:
        if guess == the_number:
            print("Gratulacje, udało Ci się zgadnąć za", tries, "razem!")
        break
    else:
        print("Niestety nie udało Ci się zgadnąć w maksymalnie 5 próbach.")
        break
    
#Zamknięcie programu
print("\n\nAby zakończyć program, naciśnij enter.")
