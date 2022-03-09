def multiplyMatrix(A, B):
    result = []
    for j in range(len(A)):
        result.append([])
        result[i] = [0] * len(B[0])
        for i in range(len(B[0])):
            result[i][j] = 0
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mitjana(sequence):
    suma = 0
    i = 0
    for i in range(len(sequence)):
        suma += sequence[i]

    return suma/(i+1)

def sumatori(sequence):
    i = 0
    suma = 0
    m = mitjana(sequence)
    while i < len(sequence):
        suma += pow(sequence[i] - m, 2)
        i += 1
    return suma

sequence = [1, 2, 3, 4]
print(sumatori(sequence))