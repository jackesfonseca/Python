matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz)

print("Linha 1: {}".format(matriz[0]))
print("Linha 2: {}".format(matriz[1]))
print("Coluna 1 linha 1: {}".format(matriz[0][0]))

for i in range(0, 3):
    print(matriz[i])

for i in range(0, 3):
    for j in range(0, 3):
        print(matriz[i][j])
