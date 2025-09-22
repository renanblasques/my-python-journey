import random as rnd

numeros = list(range(100))
rnd.shuffle(numeros)
cartela = [numeros[i*5:(i+1)*5] for i in range(5)]

for linha in cartela:
    print(" ".join(map(str, linha)))
