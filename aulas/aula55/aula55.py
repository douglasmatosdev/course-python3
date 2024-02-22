"""
Imprecisão de pontos flutuantes
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

import decimal


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 2))
print(round(numero_3, 3))
print(round(numero_3, 10))

print(20 * "-")

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
print(round(numero_3, 3))
print(round(numero_3, 10))
