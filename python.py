import math

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

#Funkcja zip() łączy elementy z wielu iterowalnych obiektów (np. list) w krotki. Przestaje działać, gdy najkrótszy z obiektów się skończy.
#https://docs.python.org/3/library/functions.html#zip
polaczone = list(zip(lista1, lista2))
print("Połączone listy (zip):", polaczone)

#Moduł math zawiera funkcje matematyczne, takie jak pierwiastek (sqrt()), funkcje trygonometryczne, logarytmy itp.
#https://docs.python.org/3/library/math.html
liczba = 16
pierwiastek = math.sqrt(liczba)
print(f"Pierwiastek kwadratowy z {liczba} to {pierwiastek}")

#Wyjątek ZeroDivisionError jest podnoszony, gdy próbujemy podzielić liczbę przez zero.
#https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
try:
    wynik = 10 / 0
except ZeroDivisionError as e:
    print("Błąd:", e)

