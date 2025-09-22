import numpy as np

mat = []
n = int(input().strip())

for i in range(n):
    line = list(map(int, input().strip().split()))
    mat.append(line)

mat_np = np.array(mat).astype(int)
trace = np.trace(mat_np)

print(trace)