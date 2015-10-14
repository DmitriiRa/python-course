def euclid(a, b):
    while a != b:
        if (a < b):
            c = a
            a = b
            b = c
        else:
            a -= b
    return a


numbers = input().split()
a = int(numbers[0])
b = int(numbers[1])

print(euclid(a, b))
