valores = []
for _ in range(10):
    valores.append(int(input()))

soma = 0
for i in range(10):
    if i % 2 == 1:
        soma += valores[i]

print(soma)