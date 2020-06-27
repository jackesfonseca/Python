#importações
import math

print(math.sqrt(25))

#Imprimir dados formatados
pi = 3.14159265
print("PI value is: {:.2f}".format(pi))#.format está disponível apenas a parti do python 3

#Entrada de dados

#OBS: o input sempre ler como uma string, por isso, deve-se fazer o suo de conversão explícita na leitura de oputros tipos de dados
x = int(input('enter with a number: '))#dentro dos parênteses pode ser usado ("" ou '') 

print(x)
#Comando de repetição
a, b = 0, 5#dupla atribuição

while a < 5:
    print(a)
    a = a + 1

lista = ['p', 'y', 't', 'h', 'o', 'n']#atribuição manual de lista

for item in lista:
    item = item.replace('\n', '')
    print(item)

#Comando condicional
if a > 5:
    print("a* is bigger than five")
elif a < 5:
    print("a* is not bigger than five")
else:
    print("a* worth as much as five")

#funções
i = 1
j = 1

def addTwo(i, j):
    k = i + j
    return k

addTwo(i , j)

