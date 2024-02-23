"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

# string = 'Luiz Otávio'
# outra_variavel = string
# string[3] = 'ABC' # vai dar erro pois não é possível alterar uma string
# print(string[3])

string = "Luiz Otávio"
outra_variavel = f"{string[:3]}ABC{string[4:]}"
print(outra_variavel)

string = "luiz Otávio"
string.capitalize()
print(string)
