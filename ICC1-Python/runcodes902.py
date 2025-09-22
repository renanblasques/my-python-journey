matriz = []
for i in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

somas = [0]*5
for j in range(5):
    for i in range(4):
        somas[j] += matriz[i][j]

print(*somas)