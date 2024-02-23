"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# como o 'for' faz por debaixo dos panos
# for letra in texto
texto = "Luiz"  # iterável
iterador = iter(texto)  # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
# a implementação de cima é a mesma da implementação de baixo
for letra in texto:
    print(letra)
# texto = iter("Luiz")  # texto = 'Luiz'.__iter__
# print(iter(texto))  # print(texto.__next__())
# print(iter(texto))  # print(texto.__next__())
# print(iter(texto))  # print(texto.__next__())
# print(iter(texto))  # print(texto.__next__())
# print(iter(texto))  # print(texto.__next__()) # Erro

# numeros = range(0, 100, 8)
# for numero in numeros:
#     print(numero)
