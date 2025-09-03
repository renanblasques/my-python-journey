n1 = int(input())
n2 = int(input())
op = input()

if op == '+':
    sum = n1 + n2
    print(sum)
elif op == '-':
    sub = n1 - n2
    print(sub)
elif op == '*':
    mult = n1 * n2
    print(mult)
elif op == '/':
    if n2 == 0:
        print("Erro: divisao por zero")
    else:
        div = n1 / n2
        print(f"{div:.2f}")
else:
    print("Erro: operacao invalida")