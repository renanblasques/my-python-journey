n = 1
positivos = 0
negativos = 0
soma_positivos = 0
soma_negativos = 0
soma_total = 0

while n != 0:
    n = float(input())
    if n > 0:
        positivos = positivos + 1
        soma_positivos = soma_positivos + n
        continue
    if n < 0:
        negativos = negativos + 1
        soma_negativos = soma_negativos + n

soma_total = soma_negativos + soma_positivos

print(f"Numero de valores positivos: {positivos}")
print(f"Numero de valores negativos: {negativos}")
print(f"Soma dos valores positivos: {soma_positivos:.1f}")
print(f"Soma dos valores negativos: {soma_negativos:.1f}")
print(f"Soma total: {soma_total:.1f}")