""" while/else """

string = "Valor qualquer"

i = 0
while i < len(string):
    letra = string[i]

    # break
    if letra == " ":
        break

    print(letra)
    i += 1
else:  # se encontrar um break o else não vai ser executdo
    print("Não encontrei um spaço na string.")  # print("O 'else' foi executado.")
print("Fora do while")
