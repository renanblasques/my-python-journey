contador_lancamentos = 0
seis_consecutivos = 0

while seis_consecutivos < 3:
    numero = int(input())

    if numero < 1 or numero > 6:
        print("Numero invalido! Digite um numero entre 1 e 6.")
        continue

    contador_lancamentos += 1

    if numero == 6:
        seis_consecutivos += 1
    else:
        seis_consecutivos = 0

print(f"Voce conseguiu 3 seis consecutivos em {contador_lancamentos} lancamentos!")