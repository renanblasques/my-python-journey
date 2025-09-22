matriz = []
for i in range(5):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(5):
    matriz[i][2], matriz[2][i] = matriz[2][i], matriz[i][2]

for i in range(5):
    print(*matriz[i])