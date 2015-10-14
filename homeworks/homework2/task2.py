# простые числа
def prime(number):
    if number == 1:
        return False
    mod = 1
    i = number
    while mod != 0:
        mod = number % (i - 1)
        i = i - 1
        if i == 1:
            return True
    return False

quantity = int(input())
resault = []

for j in range(quantity):
    n = int(input())
    resault.append(prime(n))

for j in range(quantity):
    print(resault[j])
