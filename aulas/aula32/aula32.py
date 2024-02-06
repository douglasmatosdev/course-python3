"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Exemplo 1
entrada = input("Digite um número: ")
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = "Ímpar"

    if par_impar:
        par_impar_texto = "Par"

    print(f"O número {entrada_int} é {par_impar_texto}")
else:
    print("Você não digitou um inteiro")

# Exemplo 2
# entrada = input("Digite um número: ")
# try:
#     if entrada.isdigit():
#         entrada_int = int(entrada)
#         par_impar = entrada_int % 2 == 0
#         par_impar_texto = "Ímpar"

#         if par_impar:
#             par_impar_texto = "Par"

#         print(f"O número {entrada_int} é {par_impar_texto}")
#     else:
#         print("Você não digitou um inteiro")
# except:
#     print("Você não digitou um inteiro")

# Exemplo 3
# value = input("Digite um número inteiro: ")
# try:
#     intValue = int(value)
#     if value and isinstance(intValue, int):  # if value and type(value) is int:
#         is_even = intValue % 2 == 0  # par
#         if is_even:
#             print("Par")
#         else:
#             print("Ímpar")
#     else:
#         print("Não é um inteiro.")
# except:
#     print("Não é um inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# Exemplo 1
value2 = input("Informe as horas: ")

if value2.isdigit():
    intValue2 = int(value2)

    if intValue2 >= 0 and intValue2 <= 11:
        print("Bom dia")
    elif intValue2 >= 12 and intValue2 <= 17:
        print("Boa tarde")
    elif intValue2 >= 18 and intValue2 <= 23:
        print("Boa noite")
    else:
        print("Não conheço essa hora")
else:
    print("Por favor, digite apenas números inteiros")

# Exemplo 2
# value2 = input('Informe as horas: ')
# try:
#     intValue2 = int(value2)

#     if intValue2 >= 0 and intValue2 <= 11:
#         print("Bom dia")
#     elif intValue2 >= 12 and intValue2 <= 17:
#         print("Boa tarde")
#     elif intValue2 >= 18 and intValue2 <= 23:
#         print("Boa noite")
#     else:
#         print("Não conheço essa hora")
# except:
#     print("Por favor, digite apenas números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se tiver 4 letras ou
menos escreva "Seu nome é curto"; se estiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input("Digite seu nome: ")
tamanho = len(nome)
if tamanho > 1:
    if tamanho <= 4:
        print("Seu nome é curto")
    elif tamanho >= 5 and tamanho <= 6:
        print("Seu nome é normal")
    elif tamanho > 6:
        print("Seu nome é muito grande")
else:
    print("Digite mais de uma letra")

# value3 = input("Informe seu primeiro nome: ")

# lenth = len(value3)
# if lenth <= 4:
#     print("Seu nome é curto")
# elif lenth >= 5 and lenth <= 6:
#     print("Seu nome é normal")
# elif lenth > 6:
#     print("Seu nome é muito grande")
