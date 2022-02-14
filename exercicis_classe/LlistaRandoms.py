import random

def generarLlista(n):
    i = 0
    suma = 0
    llista = []
    while i < n:
        num = random.randint(0, 100)
        llista.append(num)
        i += 1
    return llista

def sumarLlista(llista):
    i = 0
    suma = 0
    while i < len(llista):
        suma += llista[i]
        i += 1
    return suma

def mitjanaLlista (suma, n):
    return suma/n


print("Aquest programa generarà una llista de n nombre aleatoris i calcularà la seva suma, mitjana, valor màxim i el valor mínim\n"
      "Introdueix la mida n de la llista: ")
n = int(input())

llista = generarLlista(n)
suma = sumarLlista(llista)
mitjana = mitjanaLlista(suma, n)
print(llista, "suma:", suma)
print("mitjana: ", mitjana)