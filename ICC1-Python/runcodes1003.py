import numpy as np

n = int(input())

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

vector_a = np.array(a)
vector_b = np.array(b)

dot_product = np.dot(vector_a, vector_b)

print(dot_product)