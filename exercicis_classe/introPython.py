
def suma():
    result = 0
    print("Introdueix el primer numero:")
    num1 = int(input())
    print("Introdueix el segon numero:")
    num2 = int(input())
    result = num1 + num2
    print(num1, "+", num2, "=", result)

#suma()

def sumaEnters():
    print("Introdueix un nombre enter:")
    num = int(input())
    suma = 0
    for i in range(num + 1):
        suma = suma + i
    print("El resultat de la suma es: ", suma)

#sumaEnters()

def sumaParells():
    print("Introdueix un nombre enter")
    num = int(input())
    suma = 0
    i = 0
    while i <= num:
        if i % 2 == 0:
            suma = suma + i
        i += 1
    print("El resumtat de la suma dels parells es: ", suma)

#sumaParells()

def sumaRecursiva(n, suma):
    if n == 0:
        return print("La suma es:", suma)
    else:
        sumaRecursiva(n - 1, suma + n)

#print("Introdueix un nombre: ")
#n = int(input())
#sumaRecursiva(n, 0)

