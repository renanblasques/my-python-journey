valores = []
for _ in range(5):
    valores.append(int(input()))

inversa = []
for i in range(4, -1, -1):
    inversa.append(valores[i])

print(*inversa)