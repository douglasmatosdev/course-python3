nome = "Douglas Matos"
altura = 1.66
peso = 73
imc = ...  # IMC = peso / (altura x altura)

# Douglas Matos tem 1.66 de alura,
# pesa 95 quilos e seu IMC é
# 26.491508201480624

# imc = peso / (altura * altura)
imc = peso / (altura**2)

# f-strings
linha_1 = f"{nome} tem {altura:.2f} de altura"
linha_2 = f"pesa {peso} quilos e seu IMC é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
