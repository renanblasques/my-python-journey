matriz = []
for i in range(4):
    linha = list(map(int, input().split()))
    matriz.append(linha)

A, B = map(int, input().split())

cont = 0
for i in range(4):
    for j in range(5):
        if A <= matriz[i][j] <= B:
            cont += 1

print(cont)