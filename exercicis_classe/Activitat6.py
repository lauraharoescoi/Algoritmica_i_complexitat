def sumSubarrayRecursiu(array, max):
    if len(array) <= 1:
        return max
    if max < (array[0] + array[1]):
        max = array[0] + array[1]
    return sumSubarrayRecursiu(array[1:], max)

def sumSubarrayIteratiu(array, max):
    while len(array) > 1:
        if max < array[0] + array[1]:
            max = array[0] + array[1]
        array = array[1:]
    return max

array = [1, 2, 4, -3, 9, -6, 4, 8, 9, -5]
print(sumSubarrayRecursiu(array, 0))
print(sumSubarrayIteratiu(array, 0))
