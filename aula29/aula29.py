"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# print(123)
# print(456)
# int('b') #  int('b') ValueError: invalid literal for int() with base 10: 'b'


numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
except:
    print("Isso não é um número")

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f"O dobro de {numero_str} é {numero_float * 2:.2f}")
# else:
#     print("Isso não é um número")
