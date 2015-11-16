def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n


def combinations(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    if n > k:
        return(int(factorial(n) / factorial(k) / factorial(n - k)))


with open("dict.txt") as f:
    noun = 0
    adj = 0
    verb = 0
    for word in f:
        if word.endswith("ka\n"):
            noun += 1
        elif word.endswith("yo\n"):
            adj += 1
        else:
            verb += 1

#    print("noun", noun)
#    print("adj", adj)
#    print("verb," verb)

    var_of_adj = 0
    if adj > 7:
        k = 7
    else:
        k = adj
    for i in range(k):
        var_of_adj += combinations(k, i + 1) * factorial(i + 1)
    res = noun * verb * var_of_adj
    print(res)
