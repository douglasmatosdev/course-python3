"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print("Valor" if True else "Outro valor")
print("Valor" if False else "Outro valor")

print()
print(50 * "-")
print()

condicao = 10 == 10
variavel = "Valor" if condicao else "Outro valor"
print(variavel)

condicao = 10 == 11
variavel = "Valor" if condicao else "Outro valor"
print(variavel)

print()
print(50 * "-")
print()

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

digito = 10
novo_digito = digito if digito <= 9 else 0
print(novo_digito)

print()
print(50 * "-")
print()

print("Valor" if False else "Outro valor" if False else "Fim")
