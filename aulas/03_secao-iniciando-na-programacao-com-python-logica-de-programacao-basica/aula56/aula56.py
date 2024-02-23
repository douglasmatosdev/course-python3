"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = "Olha só que, coisa interessante"
lista_frases = frase.split()
print(lista_frases)

print(50 * "-")

frase = "Olha só que, coisa interessante"
lista_frases = frase.split(",")
print(lista_frases)

print(50 * "-")

frase = "Olha só que, coisa interessante"
for i, frase in enumerate(lista_frases):
    print(lista_frases[i])

print(50 * "-")

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())  # remove espaços da equerada e da direita

print(50 * "-")

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].rstrip())  # remove espaços da direita

print(50 * "-")

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].lstrip())  # remove espaços da esquerda

print(50 * "-")


frase = "Olha só que, coisa interessante"
lista_frases = frase.split(",")
for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()
print(lista_frases)

print(50 * "-")

frase = "Olha só que, coisa interessante"
lista_frases_cruas = frase.split(",")
lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
print(lista_frases)

print(50 * "-")

frases_unidas = "".join("abc")
print(frases_unidas)

print(50 * "-")

frases_unidas = "-".join("abc")
print(frases_unidas)

print(50 * "-")

frases_unidas = "-".join(lista_frases)
print(frases_unidas)

print(50 * "-")

frases_unidas = ", ".join(lista_frases)
print(frases_unidas)
