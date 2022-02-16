def producte_intuitiu(n1, n2):
    resultat = 0
    while n1 > 0:
        resultat += n2
        n1 -= 1
    return resultat

def producte_eficient(n1, n2):
    resultat = 0
    while n1 > 0:
        if n1 % 2 == 1:             #sol es sumen els senars
            resultat += n2
        n1 = n1 // 2                #divisió entera
        n2 = n2 * 2
    return resultat

print("Introdueix el primer nombre: ")
n1 = int(input())
print("Introdueix el segon nombre: ")
n2 = int(input())

print("La seva multiplicacio es ", producte_intuitiu(n1, n2))


#   ENSAMBLADOR DEL PRODUCTE EFICIENT

#   DATA result
#   MOVE result 0   #3 cycles

#   while:
#           CMP x 0  #2 cycles
#           BRANCH_EQUAL endwhile  #5 cycles
#           MOVE aux x  #3 cycles
#           AND aux 1   #3 cycles
#           CMP aux 0   #2 cycles
#           BRANCH_EQUALS endif #5 cycles
#           ADD result y    #3 cycles
#       endif
#           SHIFT_RIGHT x   #2 cycles
#           SHIFT_LEFT y    #2 cycles
#       GOTO while  #5 cycles

#       endwhile