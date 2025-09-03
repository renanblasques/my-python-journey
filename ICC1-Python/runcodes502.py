cont_notas_baixas = 0
cont_notas_altas = 0
soma_total = 0

nota_atual = float(input())

while (nota_atual >= 0):
    if (nota_atual >= 5):
        cont_notas_altas += 1
    else:
        cont_notas_baixas += 1
    soma_total += nota_atual
    nota_atual = float(input())

cont_total = cont_notas_altas + cont_notas_baixas
media = soma_total / cont_total
percentual_altas = (cont_notas_altas / cont_total) * 100
        
print(f"Baixas: {cont_notas_baixas}")
print(f"Altas: {cont_notas_altas}")
print(f"Media: {media:.2f}")
print(f"Percentual: {percentual_altas:.0f}%")