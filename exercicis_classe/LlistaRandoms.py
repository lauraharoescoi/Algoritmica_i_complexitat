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

def mitjanaLlista (llista, n):
    return sumarLlista(llista)/n

def minim (llista):
    min = llista[0]
    i = 0
    while i < len(llista):
        if min > llista[i]:
            min = llista[i]
        i += 1
    return min

def maxim (llista):
    max = llista[0]
    i = 0
    while i < len(llista):
        if max < llista[i]:
            max = llista[i]
        i += 1
    return max

print("Introdueix la mida de la llista de nombres aleatoris del 0 al 100: ")
n = int(input())
llista = generarLlista(n)

print("Que vols obtenir:\n"
      "  a (suma)\n"
      "  b (mitjana)\n"
      "  c (valor mínim)\n"
      "  d (valor màxim")
opcio = input()

if opcio == 'a':
    print("La suma de la llista ", llista, "es ", sumarLlista(llista))

elif opcio == 'b':
    print("La mitjana de la llista ", llista, "es", mitjanaLlista(llista, n))

elif opcio == 'c':
    print("El minim valor de la llista ", llista, "es", minim(llista))

elif opcio == 'd':
    print("El maxim valor de la llista ", llista, "es", maxim(llista))

else:
    print("Opcio no valida")
