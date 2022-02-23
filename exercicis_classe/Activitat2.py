

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

def bubbleSortOptim(theArray)
    changed = False
    while changed:
        for i in range(len(theArray) - 1):
            if theArray[i] > theArray[i + 1]:
                theArray[i], theArray[i + 1] = theArray[i + 1], theArray[i]
                changed = True


theArray = [2, 4, 7, 1, 3]
print(bubbleSort(theArray))

#   ENSAMBLADOR DEL BUBBLESORT

#   DATA theArray
#   DATA temp
#   DATA i
#   DATA j

#   MOVE j arrayLength
#   for2:
#       DEC j
#       CMP j 0
#       BRANCH_SMALLER_EQ final
#       MOVE i 0
#       for1:
#           CMP i j
#           BRANCH_EQUAL endfor  #5 cycles
#           CMP theArray[i] theArray[i + 1]
#           BRANCH_SMALLER_EQ noSwap
#           MOVE temp theArray[i]
#           MOVE theArray[i] theArray[i + 1]
#           MOVE theArray[i + 1] temp
#       noSwap:
#           INC i
#           GOTO for1
#       endfor
#       GOTO for2
#   final