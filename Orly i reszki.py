# Program "rzuca" 100 razy monetą, a następnie podaje liczbę orzełków i reszek

#Importowanie
import random

#Powitanie
print("Witaj w programie RZUT MONETĄ.")
print("Teraz rzucimy monetą 100 razy...\n")

#Rzucanie monetą
orzelek = 0
reszka = 0
wartosc = 0
while wartosc < 100:
    rzut = random.randint(0,1)
    if rzut == 0:
        print("Orzelek")
        orzelek += 1
    else:
        print("Reszka")
        reszka += 1
    wartosc += 1

#Podanie liczby orzełków i reszek
print("Po rzuceniu 100 razy monetą uzyskaliśmy ", orzelek, "orzełków oraz ", reszka, "reszek.")

#Zakończenie programu
input = print("\n\nJeśli chcesz zakończyć program, wciśnij enter.")
