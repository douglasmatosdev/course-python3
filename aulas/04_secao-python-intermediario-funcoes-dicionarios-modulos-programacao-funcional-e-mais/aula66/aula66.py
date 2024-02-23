"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):  # definição
#     print(x + y)
# print(soma(1, 2)) # retorna 3 e None


# def soma(x, y):  # definição
#     print(f"{x=} y={y}", "|", "x + y =", x + y)
# soma(1, 2)
# soma(2, 1)
# soma(y=2, x=1)


def soma(x, y, z):  # definição
    print(f"{x=} y={y} {z=}", "|", "x + y + z =", x + y + z)


soma(1, 2, 3)
soma(y=2, z=3, x=1)
print(1, 2, 3, sep="-")
soma(1, 2, z=5)
