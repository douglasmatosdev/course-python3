"""
Operadores de atribuição
 = += -= *= /= //= **= %=
"""

contador = 0

while contador <= 10:
    contador = contador + 1
    print(contador)

print("Acabou")

contador += 2
print(contador)
contador = 3
print(contador)
contador *= "2"
print(contador)
contador = 10
contador %= 2
print(contador)
contador = 2
contador **= 10
print(contador)
contador /= 2
print(contador)
contador //= 3
print(contador)
