"""
For + Range
range -> range(start, stop, step)
"""

# numeros = range(10)
# print(numeros)
# numeros = range(5, 10)
# print(numeros)
# numeros = range(5, 10, 2)
# print(numeros)


numeros = range(10)
for numero in numeros:
    print(numero)

numeros = range(0, -10, -1)
for numero in numeros:
    print(numero)


numeros = range(0, 100, 8)
for numero in numeros:
    print(numero)
