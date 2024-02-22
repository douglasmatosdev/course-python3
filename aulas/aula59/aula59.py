# Desempacotamento em chamadas
# de métodos e funções
string = "ABCD"
lista = ["Maria", "Helena", "Eduarda"]
tupla = "Python", "é", "legal"
salas = [
    # 0
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1      2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)], # 2
]


a, b, c = lista
print(a, b)

print(20 * "-")

lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
primeiro, b, *_, ultimo = lista
print(primeiro, ultimo)

print(20 * "-")

lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
primeiro, segundo, *_, antipenultimo, ultimo = lista
print(primeiro, segundo, antipenultimo, ultimo)

print(20 * "-")
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
for nome in lista:
    print(nome, end=" ", sep=" ")

print() # apenas para quebrar linha

for nome in lista:
    print(nome, end=" ")

print() # apenas para quebrar linha


# Isso 
print("Maria", "Helena", 1, 2, 3, "Eduarda")
## é igual a isso
print(*lista)
print(*string)
print(*tupla)
print() # apenas para quebrar linha
print(salas)
print() # apenas para quebrar linha

print(*salas)
print() # apenas para quebrar linha

print(*salas, end='\n')
print() # apenas para quebrar linha


print(*salas, sep='\n')
print() # apenas para quebrar linha