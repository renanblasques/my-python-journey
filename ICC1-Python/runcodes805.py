A = []
B = []

for _ in range(5):
    A.append(int(input()))
for _ in range(5):
    B.append(int(input()))

iguais = 1
for i in range(5):
    if A[i] != B[i]:
        iguais = 0
        break

print(iguais)