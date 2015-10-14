# сочетания
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

numbers = input().split()
n = int(numbers[0])
k = int(numbers[1])
print(combinations(n, k))
