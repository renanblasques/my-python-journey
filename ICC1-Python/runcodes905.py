matriz = []
for i in range(5):
    linha = list(map(int, input().split()))
    matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]
imax=jmax=imin=jmin=0

for i in range(5):
    for j in range(5):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            imax, jmax = i, j
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            imin, jmin = i, j

print(maior, imax, jmax)
print(menor, imin, jmin)