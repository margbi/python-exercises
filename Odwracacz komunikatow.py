# Program, który wczytuje komunikat użytkownika, a następnie wypisuje go w odwrotnej kolejności

# Powitanie
print("Witaj w programie, który wczyta Twój komunikat i wyświetli go w odwrotnej kolejności.\n")

#Pobranie komunikatu od użytkownika
komunikat = input("Wpisz swój komunikat: ")

#Wyświetlanie komunikatu w odwrotnej kolejności
print("Twój komunikat w odwróconej kolejności brzmi następująco:", komunikat[::-1])

#Zamknięcie programu
input("\nJeśli chcesz zakończyć program, wciśnij enter.")