import sys
import matplotlib.pyplot as plt
from random import sample, choice, shuffle

def tableGenerator(number_reserves):
    wing_types = map(lambda x: x + '-Reserva', ['JUAN', 'PEPE', 'MARIA', 'LAIA', 'MONTSE', 'PAULA'])
    L = list(wing_types)
    free_pos = sample(range(number_reserves), number_reserves >> 1)
    position = 0

    global solution
    solution = min(free_pos)

    while position <= number_reserves:
        if position not in free_pos:
            yield choice(L), str(position)
        position += 1

def reserveList (number_reserves):

    reserve_list = [i for i in tableGenerator(number_reserves * 2)]

    reserve_list = reserve_list[:number_reserves]

    shuffle(reserve_list)

    return reserve_list, solution


def bookerineManagement_iterativo(reserves):

    idTable = -1

    #Your code here...

    return idTable

def bookerineManagement_recursivo(reserves):

    idTable = -1

    #Your code here...

    return idTable


def calcular_temps_iterativo():
    import timeit
    temps = []
    for x in range(0,200,10):
        temps.append( (x, timeit.timeit("bookerineManagement_iterativo("+str(x)+")",
            setup="from __main__ import bookerineManagement_iterativo")) )
    return temps

def calcular_temps_recursivo():
    import timeit
    temps = []
    for x in range(0,200,10):
        temps.append( (x, timeit.timeit("bookerineManagement_recursivo("+str(x)+")",
            setup="from __main__ import bookerineManagement_recursivo")) )
    return temps


def crear_grafica( x_list, y_list ):
    plt.scatter(x_list, y_list)
    plt.show()


def costEmpiricalComputation ():

    temps_iterativo = calcular_temps_iterativo()
    crear_grafica(*map(list, zip(*temps_iterativo)))

    temps_recursivo = calcular_temps_recursivo()
    crear_grafica(*map(list, zip(*temps_recursivo)))

    return 0

# Programa Principal para la generación de mesas y reservas dentro de un restaurante. Para ello, al programa deberemos
# de pasarle como argumentos el tamaño del restaurante en número de mesas.
if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit('Usage: ' + sys.argv[0] + ' <list_size>')

    out_reserves = reserveList(int (sys.argv[1]))
    reserves = out_reserves [0]
    idTable = bookerineManagement_iterativo(reserves)

    costEmpiricalComputation()

    if idTable == solution:
        print ('Solucion Correcta')
    else:
        print ('Solucion Incorrecta')
