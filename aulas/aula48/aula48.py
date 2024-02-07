"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append  - Adiciona um item no final
    insert  - Adiciona um item no índice escolhido
    pop     - Remove do final ou do índice escolhido
    del     - Apaga um índice
    clear   - Limpa a lista
    extend  - Estende a lista
    +       - Concatena listas
Create  Read    Update  Delete (CRUD)
Cria    Ler     Alterar Apagar
"""

#          +01234
#          -54321
string = "ABCDE"  # 5 caracteres (len)
# lista = []
# print(bool(lista))
# print(lista, type(lista))
#          0     1       2                3     4
#         -5    -4      -3               -2    -1
lista = [123, True, "Luiz Otávio", 1.2, []]
print(lista)
print(lista[-3])
lista[-3] = "Maria"
print(lista[-3])
print(lista[2], type(lista[2]))
print(lista)

print(f'\n{20 * "*"}\n')

lista = [1, 2, 3, 4]
print(lista)
numero = lista[2]
print(numero)

print(f'\n{20 * "*"}\n')

#          0   1    2    3   4    5
lista = [10, 20, 30, 40, 50, 60]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2])
print(lista)

print(f'\n{20 * "*"}\n')

lista = [10, 20, 30, 40]
print(lista)
lista.append(50)
print(lista)
ultimo_valor = lista.pop()
print(lista, "Removido,", ultimo_valor)
removido = lista.pop(2)
print(lista, "Removido,", removido)

print(f'\n{20 * "*"}\n')

#          0   1    2    3
lista = [10, 20, 30, 40]
print(lista)

lista.append("Luiz")
print(lista)

nome = lista.pop()
print(lista)

lista.append(1233)
print(lista)

del lista[-1]
print(lista)

lista.clear()
print(lista)

lista = [10, 20, 30, 40]
lista.insert(0, 5)
print(lista)

print(f'\n{20 * "*"}\n')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
lista_d = [0]
lista_d.extend(lista_a)
print(lista_d)
lista_e = lista_d + lista_b
print(lista_e)

print(f'\n{20 * "*"}\n')

print(
    """
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
\n"""
)

lista_a = ["Luiz", "Maria"]
lista_b = lista_a
print("Antes - Lista a:", lista_a)
print("Antes - Lista b:", lista_b)
lista_a[0] = "Qualquer coisa"
print("Depois - Lista a:", lista_a)
print("Depois - Lista b:", lista_b)

print(f'\n{20 * "*"}\n')

lista_a = ["Luiz", "Maria", 1, True, 1.2]
lista_b = lista_a.copy()  # Shallow
print("Antes - Lista a:", lista_a)
print("Antes - Lista b:", lista_b)
lista_a[0] = "Qualquer coisa"
print("Depois - Lista a:", lista_a)
print("Depois - Lista b:", lista_b)
