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


llista = generarLlista(5)
suma = sumarLlista(llista)
print(llista, "suma:", suma)