"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

MULTIPLY_BY = 10
PART_ONE_LENGTH = 9
TOTAL_LENGTH = 11
cpf_input = "746.824.890-70"
cpf_partes = cpf_input.split("-")
cpf_parte_um, cpf_parte_dois = cpf_partes
cpf_parte_um_limpo = cpf_parte_um.replace(".", "")

if len(cpf_parte_um_limpo) == 9:
    result = 0

    for index in range(10):
        by = MULTIPLY_BY - index
        if index < len(cpf_parte_um_limpo):
            result += by * int(cpf_parte_um_limpo[index])


    result *= MULTIPLY_BY
    result = result % TOTAL_LENGTH
    if result > PART_ONE_LENGTH:
        result = 0
    print(f'O primeiro digito é {result}')
else:
    print("CPF inválido")
