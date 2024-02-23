a = "A"
b = "B"
c = 1.1
formato = "a={} b={} c={}".format(a, b, c)

minha_string = "a={} b={} c={}"
formato2 = minha_string.format(a, b, c)

minha_string2 = "a={} b={} c={:.2f}"
formato3 = minha_string2.format(a, b, c)

minha_string3 = "a={0} a={0} a={0} b={1} c={2:.2f}"  # pegando pelo indice
formato4 = minha_string3.format(a, b, c)

minha_string4 = "a={nome1} a={nome1} b={nome2} c={nome3:.2f}"  # pegando pelo indice
formato5 = minha_string4.format(nome1=a, nome2=b, nome3=c)

print(formato)
print(formato2)
print(formato3)
print(formato4)
