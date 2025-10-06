import numpy as np

n, m = map(int, input().split())

data = []
for _ in range(n):
    row = list(map(int, input().split()))
    data.append(row)

matriz = np.array(data)

print("Matriz de producao:")
print(matriz)

soma_total = np.sum(matriz)
media_geral = np.mean(matriz)
soma_linhas = np.sum(matriz, axis=1)
soma_colunas = np.sum(matriz, axis=0)
maior_valor = np.max(matriz)
menor_valor = np.min(matriz)

print(f"\nSoma total: {soma_total}")
print(f"Media geral: {media_geral:.2f}")
print(f"Soma por linha: {soma_linhas}")
print(f"Soma por turno: {soma_colunas}")
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")