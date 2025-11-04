import math

def mdc(a, b, c):
    return math.gcd(math.gcd(a, b), c)

def mmc(a, b, c):
    def mmc_dois(x, y):
        return abs(x * y) // math.gcd(x, y)
    return mmc_dois(mmc_dois(a, b), c)

a = int(input())
b = int(input())
c = int(input())

print("MDC:", mdc(a, b, c))
print("MMC:", mmc(a, b, c))
