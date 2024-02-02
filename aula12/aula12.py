nome = "Douglas Matos"
altura = 1.66
peso = 73
imc = ...  # IMC = peso / (altura x altura)

# Douglas Matos tem 1.66 de alura,
# pesa 95 quilos e seu IMC é
# 26.491508201480624

# imc = peso / (altura * altura)
imc = peso / (altura**2)
print(nome, "tem", altura, "de altura,")
print("pesa", peso, "quilos e seu IMC é")
print(imc)
