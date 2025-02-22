# Write a program that takes the number nn from the input and calculates and displays its factorial.
# The factorial means a number like nn which is denoted by the symbol n!n! is shown; The multiplication of numbers is 11 to nn. In other words:
# n!=1×2×3×⋯×n
# input
# In one line you will be given the number nn.
# 1≤n≤10

n = int (input())


def fact (n):
    if n == 0 or n == 1:
        return 1
    else:
        r = n * fact(n - 1)

    return r

print(fact(n))