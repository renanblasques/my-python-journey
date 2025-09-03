n = int(input())
pi = 0

for i in range(n):
    if i % 2 == 0:
        pi = pi + (4.0 / ((2 * i ) + 1))
    else:
        pi = pi - (4.0 / ((2 * i ) + 1))

print(f"{pi:.6f}")