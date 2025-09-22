import numpy as np

size = list(map(int, input().strip().split()))
n = size[0]
m = size[1]

mat = []

for i in range(n):
    line = list(map(int, input().strip().split()))
    mat.append(line)

mat_np = np.array(mat).astype(int)

new_size = int(input())
k = new_size

if (n * m) != (k * k):
    print("Aviso: perda de elementos no reshape")
    mat_np = mat_np.flatten()[:k*k]

mat_np_reshape = np.reshape(mat_np, (k, k))
mat_np_t = np.transpose(mat_np_reshape)

for l in mat_np_t:
    print(*l)