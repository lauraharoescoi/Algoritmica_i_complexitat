

def swap(a, b):
    aux = theArray[a]
    theArray[a] = theArray[b]
    theArray[b] = aux

def bubbleSort(theArray):
    i = len(theArray)
    while i > 0 :
        for j in range(i - 1):
            if theArray[j] > theArray[j + 1]:
                swap(j + 1, j)
        i -= 1
    return theArray

def bubbleSortOptim(theArray):
    changed = False
    while changed:
        for i in range(len(theArray) - 1):
            if theArray[i] > theArray[i + 1]:
                theArray[i], theArray[i + 1] = theArray[i + 1], theArray[i]
                changed = True


theArray = [2, 4, 7, 1, 3]
print(bubbleSort(theArray))


#   ENSAMBLADOR DEL BUBBLESORT

#   DATA theArray 10
#   DATA temp
#   DATA i
#   DATA j
#   MOVE j arrayLength                          #3 cycles
#       for1:
#              DEC j                            #2 cycles
#              CMP j 0                          #2 cycles
#              BRANCH_SMALLER_EQ endfor1        #5 cycles
#              MOVE i 0                         #3 cycles
#       for2:
#              CMP i j                          #2 cycles
#              BRANCH_EQUAL endfor              #5 cycles
#              CMP theArray[i] theArray[i + 1]  #2 cycles
#              BRANCH_SMALLER_EQ noSwap         #5 cycles
#              MOVE temp theArray[i]            #3 cycles
#              MOVE theArray[i] theArray[i + 1] #3 cycles
#              MOVE theArray[i + 1] temp        #3 cycles
#       endif:
#              INC i                            #2 cycles
#              GOTO for2                        #5 cycles
#       endfor2:
#              GOTO for1                        #5 cycles
#       endfor1:

#   Pitjor O(n) = (3 + (12 + 14 + 9 + 7) + 5) * k + 9 = 0(n^2)
#   Millor Ω(n) = (3 + (12 + 14 + 7) + 5) * k + 9 = Ω(n^2)

#   k = sumatori de 1 a n - 1 = ((n-1) * n) / 2 = (n^2 - n) / 2