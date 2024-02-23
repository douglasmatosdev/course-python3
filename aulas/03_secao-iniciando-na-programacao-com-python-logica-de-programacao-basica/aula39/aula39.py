"""
Iterando strings com while
"""

#        01234567891011 # indices positivos
nome = "Luiz Otávio"  # Iteráveis
#        -1-2-3-4-5-6-7-8-9-10-11 # indices negativos
print(f"Primeira letra: {nome[0]}, última letra: {nome[-1]}")
tamanho_nome = len(nome)
print(f"o tamanho de {nome} é {tamanho_nome}")
print(nome[3])

# *L*u*i*z* *O*t*á*v*i*o*
nova_string = ""
i = 0
while i < len(nome):
    nova_string += f"*{nome[i]}"
    i += 1
nova_string += "*"
print(nova_string)
