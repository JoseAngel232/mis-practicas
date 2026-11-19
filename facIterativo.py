def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

print(factorial_iterativo(5))

#---------------------------------------------

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))