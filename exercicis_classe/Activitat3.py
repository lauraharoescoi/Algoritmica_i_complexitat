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
    j = 0
    for j in range(len(sequence)):
        suma += sequence[i]
    return suma/(j + 1)

def sumatoriIteratiu(sequence):
    j = 0
    suma = 0
    m = mitjana(sequence)
    while j < len(sequence):
        suma += pow(sequence[j] - m, 2)
        j += 1
    return suma

def sumatoriRecursiu(sequence, m):
    if len(sequence) == 0:
        return 0
    else:
        return (sequence[0] - m) ** 2 + sumatoriRecursiu(sequence[1:], m)

sequence = [1, 2, 3, 4]
m = mitjana(sequence)
print(sumatoriRecursiu(sequence, m))
print(sumatoriIteratiu(sequence))