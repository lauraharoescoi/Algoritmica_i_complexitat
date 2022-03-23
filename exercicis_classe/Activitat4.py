def sum_of_digits(x):
    sum = 0
    while x != 0:
        sum = sum + (x % 10)
        x = x // 10
    return sum

def multiple3recursiu(x):
    if (x > 9):
        return multiple3recursiu(sum_of_digits(x))
    if x == 0 or x == 3 or x == 6 or x == 9:
        return True
    else:
        return False

def multiple3iteratiu(x):
    while x > 9:
        x = sum_of_digits(x)
    if x == 0 or x == 3 or x == 6 or x == 9:
        return True
    else:
        return False

x = int(input("Introdueix un nombre: "))
print(multiple3recursiu(x))
print(multiple3iteratiu(x))
