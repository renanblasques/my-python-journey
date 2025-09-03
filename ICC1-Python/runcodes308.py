altura = float(input())
sexo = input().strip().upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido.")

print(f"Peso ideal: {peso_ideal:.2f} kg")