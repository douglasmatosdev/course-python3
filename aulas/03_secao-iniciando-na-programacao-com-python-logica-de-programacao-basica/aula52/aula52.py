"""
Tipo tupla - Uma lista imutável
"""

nomes = ["Maria", "Helena", "Luiz"]
nomes[1] = "outro"
_, _, nome, *resto = nomes
print(nomes)
print(nome)

# tupla
nomes = "Maria", "Helena", "Luiz"
print(nomes[2])

nomes = list(nomes) # convertendo uma tupla para lista
nomes = tuple(nomes) # convertendo uma list para tupla

