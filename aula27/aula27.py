"""
Fatiamento de strings
012345678
Olá mundo
-9-8-7-6-5-4-3-2-1
Fatiamento [inicio:fim:passo] [::]
Obs.: a função len retorna a quantidade de caracteres da string
"""

variavel = "Olá mundo"
print(len(variavel))
print(variavel[4])
print(variavel[4:])
print(variavel[4:9])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[3])
print(len(variavel[3]))
print(variavel[0 : len(variavel) : 1])
print(variavel[0:9:1])
print(variavel[0 : len(variavel) : 4])
print(variavel[::-1])
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-4])
