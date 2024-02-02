# Operador lógico "not"
# Usado par inverter expressões
# not True = False
# not False = True
print("not False =", not False)
print("not True =", not True)
print("not 0 =", not 0)
print("not 1 =", not 1)
print("not '' =", not "")
print("not 'abc' =", not "abc")

senha = input("Senha: ")

# if senha != "123456":
#     print("Senha incorreta.")

if not senha:
    print("Senha incorreta.")
