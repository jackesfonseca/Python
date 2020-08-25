  #Tuplas

tupla = ("ana", "maria", "marta")
print(tupla)
print(tupla[0])
print(tupla.index("maria"))

#lista

print()

l1 = ["rafael", "miquelangelo", "donatelo"]
l2 = ["leonardo"]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)
l2_2 = l2 * 2
print(l2_2)
print(l1[2])
print(l1[0:2])
l3.append("splinter")
print(l3)
l3.remove("splinter")
print(l3)
#del(l1) deleta a lista mas um erro é lançado

#dicionario

print()
coleta = {"ana": 19, "maria": 43, "marta" : 15}
print(coleta)
print(coleta["marta"])#irá exibir o valor referente à chave marta
coleta["amanda"] = 18
print(coleta)
del(coleta)["amanda"]
print(coleta)
print(coleta.items())
print(coleta.keys())
print(coleta.values())
coleta2 = {"pedro": 25, "alisson": 23}
coleta.update(coleta2)#concatena os dicionários
print(coleta)

for especie, num_especimes in coleta.items():
    #print("Espécie: {}, Quantidade: {}".format(especie, num_especimes))
    print("Espécie: %s, Quantidade: %d" %(especie, num_especimes))

#conjunto(set)

print()

bio = ("carboidratos", "lipideos", "proteinas", "sais minerais", "proteinas")
print(bio)
print(set(bio))#não tras os elementos repetidos

#operações com conjuntos

c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2)
print(c3)
c4 = c1.difference(c2)
print(c4)
c5 = c2.difference(c1)
print(c5)
c6 = c1.union(c2)
print(c6)















