A = []
for _ in range(10):
    A.append(int(input()))

maior_dif = 0
for i in range(1, 10):
    dif = abs(A[i] - A[i-1])
    if dif > maior_dif:
        maior_dif = dif

print(maior_dif)