#sem parâmetro e retorno
def mensagem():
    print("mensagem")

mensagem()

#com parâmetros
print()

def mensagem(texto):
    print(texto)

mensagem("função")

#com parâmetro e retorno
print()

def soma(a, b):
    return a + b

r = soma(2, 3)
print(r)

#docmentação de funções
print()

def calculaEnergiaPotencialGravitacional(m, h, g = 10):
    """
    A energia gravitacional é a energia potencial
    associada ao campo gravitacional. De acordo com
    a mecânica clássica, o potencial gravitacional
    existe entre duas ou mais massas
    """
    e = m * h * g
    return e

e = calculaEnergiaPotencialGravitacional(30, 20)

print(e)
print()
help(calculaEnergiaPotencialGravitacional)





















