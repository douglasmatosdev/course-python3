"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros
de índices inexistentes na lista.
"""

import os


list = []

while True:

    print("Selecione uma opção")
    option = input("[i]nserir [a]pagar [l]istar: ")

    if len(option) == 0:
        os.system("clear")
        print("Nada para listar")

    if option.lower() == "i":
        os.system("clear")
        value = input("Value: ")
        list.append(value)
        os.system("clear")

    elif option.lower() == "a":
        os.system("clear")

        index_str = input("Escolha o índice para apagar: ")

        try:
            index = int(index_str)
            del list[index]
        except ValueError:
            print("Por favo digite um número inteiro.")
        except IndexError:
            print("Índice não existe na lista.")
        except Exception:
            print("Erro desconhecido.")

    elif option.lower() == "l":
        os.system("clear")
        if len(list) == 0:
            print("Não há items na lista para apagar!")

        for i, value in enumerate(list):
            print(i, value)
    else:
        os.system("clear")
        print("Por favor escolhar [i], [a] ou [l]")
