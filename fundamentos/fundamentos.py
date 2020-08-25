 #importações
import math

print(math.sqrt(25))

#Imprimir dados formatados
pi = 3.14159265
print("PI value is: {:.2f}".format(pi))#.format está disponível apenas a parti do python 3
print("PI value is: %.2f" %(pi))
print("PI value is:", pi)
#Entrada de dados

#OBS: o input sempre ler como uma string, por isso, deve-se fazer o suo de conversão explícita na leitura de oputros tipos de dados
print()
x = int(input('enter with a number: '))#dentro dos parênteses pode ser usado ("" ou '') 

print(x)

#Comando de repetição
print()

a, b = 0, 5#dupla atribuição

while a < 5:
    print(a)
    a = a + 1

print();

lista = ['p', 'y', 't', 'h', 'o', 'n']#atribuição manual de lista

for item in lista:
    item = item.replace('\n', '')
    print(item)

print()

soma = 0
for i in range(1, 6):
    print(i)
    soma = soma + i

print()

print(soma)

print()

for i in range(5, 0, -1):
    print(i)

    
#Comando condicional
print()

if a > 5:
    print("a* is bigger than five")
elif a < 5:
    print("a* is not bigger than five")
else:
    print("a* worth as much as five")

#funções
print()

i = 100
j = 100

def addTwo(i, j):
    k = i + j
    print(k)

addTwo(i , j)

#manipulacao de string
print()

nome = "camisa "
maiuscula = nome.upper()
print(maiuscula)

minuscula = nome.lower()
print(minuscula)

primeiraMaiuscula = nome.capitalize()
print(primeiraMaiuscula)

comecoString = nome[0:3]
print(comecoString)

finalString = nome[3:]
print(finalString)

renomeado = nome.replace("isa","isola")
print(renomeado)

posicaoCaracter = nome.find("s")
print("Index: %d" %(posicaoCaracter))

tamanho = len(nome)
print("Length: {0}".format(tamanho))

semEspaco = nome.strip()
print("Length without space: {0}".format(len(semEspaco)))

#operadores lógicos

a = True
b = False

print("'False' and 'true' is: ", a and b)#pode usar: &
print("'False' or 'true' is: ", a or b)#pode usar: |
print("not 'False' is: ", not b)

#operadores relacionais
print()

print("5 > 3", 5 > 3)
print("5 < 3", 5 < 3)
print("5 >= 3", 5 >= 3)
print("5 <= 3", 5 <= 3)
print("5 == 3", 5 == 3)
print("5 != 3", 5 != 3)

#concatenação
print()
nome = "jackes"
idade = 19#não é possível concatenar número
print("Meu nome é " + nome)






