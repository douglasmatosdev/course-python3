"""
enumerate - enumera iteráveis (índices)
"""

lista = ["Maria", "Helena", "Luiz"]
lista.append("João")

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))
print("\n-------------------\n")

for item in lista_enumerada:
    print(item)

print("O que tem na lista enumerada: ", lista_enumerada)

for item in lista_enumerada:
    print(item)

for item in enumerate(lista):
    print(item)

lista = ["Maria", "Helena", "Luiz"]
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)  # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz')]

print("\n-------------------\n")

lista = ["Maria", "Helena", "Luiz"]
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print("\n-------------------\n")

lista = ["Maria", "Helena", "Luiz"]
for indice, nome in enumerate(lista):
    print(indice, nome)

print("\n-------------------\n")


for tupla_enumerada in enumerate(lista):
    print("FOR da tupla:")
    for valor in tupla_enumerada:
        print(f"\t{valor}")
