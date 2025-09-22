A = []
B = []

for _ in range(5):
    A.append(int(input()))
for _ in range(5):
    B.append(int(input()))

S = []
for i in range(5):
    S.append(A[i] + B[i])

print(*S)