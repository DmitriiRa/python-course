def euclid(a, b):
    while a != b:
        if (a < b):
            c = a
            a = b
            b = c
        else:
            a -= b
    return a


def pfilter(args):
    rprime = []
    for arg in (args[1:]):
        if euclid(int(args[0]), int(arg)) == 1:
            rprime.append(arg)
    return rprime
         

numbers = input().split()
res = pfilter(numbers)
if res == []:
        print("None")
else:
    for arg in res:
        print(arg, end=' ')
