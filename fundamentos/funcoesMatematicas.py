"""
Funções matemáticas

"""
from math import sqrt#trecho de código que importará o módulo sqrt do pacote math

#triângulo
print("Altura do triângulo")

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

r = (a + b) / 2

print("Altura = {0}".format(r))

#bhaskara
print()
print("Fórmula de Bhaskara")

a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b: "))
c = float(input("Informe o valor de c: "))

det = (b**2) - 4*a*c
det = sqrt(det)#caso fosse imporatado todo o pacote math seria necessário informalo de modo math.sqrt
x1 = (-b + det) /2*a
x2 = (-b - det) /2*a

print("X1 = %.2f"%(x1))
print("X2 = %.2f" %(x2))
