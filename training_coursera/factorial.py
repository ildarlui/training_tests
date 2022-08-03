def factorial(n):
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            result *= i

    print(result)


def factorial(n):
    if n == 0:
        return 1
    result = n * factorial(n - 1)
    return result

print(factorial(3))