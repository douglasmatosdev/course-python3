"""
Introdução ao desempacotamento
"""

# EXEMPLO 1
# lista = ["Maria", "Helena", "Luiz"]
# nome1, nome2, nome3 = lista
# print(nome1, nome2, nome3)

# EXEMPLO 2
# nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
# print(nome1, nome2, nome3)

# EXEMPLO 3
# nome, *resto = ["Maria", "Helena", "Luiz"]
# print(nome, resto)

# EXEMPLO 4
# nome, *_ = ["Maria", "Helena", "Luiz"]
# print(nome, _)

# EXEMPLO 5
_, nome, *_ = ["Maria", "Helena", "Luiz"]
print(_, nome, _)
