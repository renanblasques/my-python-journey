a = int(input())
b = int(input())
c = int(input())
d = int(input())

numerador = (a * d) + (c * b)
denominador = b * d

while True:
    mdc = 1
    menor = min(numerador, denominador)
    for i in range(2, menor + 1):
        if numerador % i == 0 and denominador % i == 0:
            mdc = i
    if mdc == 1:
        break
    numerador //= mdc
    denominador //= mdc

print(numerador, denominador)