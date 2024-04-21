def factorial(n):
    returned = 1
    for fac in range(n, 1 , -1):
        returned *= fac

    return returned


print(factorial(3))
print(factorial(4))
print(factorial(5))
