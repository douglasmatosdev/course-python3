# Exemplo 1
# texto = "Python"
# tamanho_string = len(texto)
# i = 0
# while i < tamanho_string:
#     print(texto[i], i)
#     i += 1

# Exemplo 2
# senha_salva = "123456"
# senha_digitada = ""
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f"Sua senha ({repeticoes}x): ")

#     repeticoes += 1

# print(repeticoes)
# print("Aquele laço acima pode ter repetições infinitas")

texto = "Python"
novo_texto = ""
for letra in texto:
    novo_texto += f"*{letra}"
    print(letra)
print(novo_texto)
