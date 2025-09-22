n = int(input())
matriz = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

soma_ref = sum(matriz[0])
ok = True

for i in range(n):
    if sum(matriz[i]) != soma_ref:
        ok = False
for j in range(n):
    if sum(matriz[i][j] for i in range(n)) != soma_ref:
        ok = False
if sum(matriz[i][i] for i in range(n)) != soma_ref:
    ok = False
if sum(matriz[i][n-1-i] for i in range(n)) != soma_ref:
    ok = False

print(1 if ok else 0)
