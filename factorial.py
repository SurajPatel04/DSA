def fact(n):
    """This function for factorial"""
    if n == 1:
        return 1
    return n * fact(n - 1)


factorial = fact(4)
print(factorial)

i = 2
k = i
print()
