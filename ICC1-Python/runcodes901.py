matriz = []
for i in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

soma = 0
for i in range(4):
    for j in range(5):
        if matriz[i][j] % 2 == 0:
            soma += matriz[i][j]

print(soma)