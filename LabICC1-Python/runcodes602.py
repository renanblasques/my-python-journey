n = int(input())
termo_anterior = 0
termo_atual = 1

if n == 1:
    print(termo_anterior)
elif n == 2:
    print(termo_anterior)
    print(termo_atual)
else:
    print(termo_anterior)
    print(termo_atual)
    for i in range(2, n, 1):
        proximo_termo = termo_anterior + termo_atual
        print(proximo_termo)
        termo_anterior = termo_atual
        termo_atual = proximo_termo