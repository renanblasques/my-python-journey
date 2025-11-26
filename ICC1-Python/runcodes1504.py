n = int(input())

for i in range(1, (n + 1), 1):
    print((i - 1) * "*\t", end="")
    print("*")

for i in range((n - 1), 0, -1):
    print((i - 1) * "*\t", end="")
    print("*")