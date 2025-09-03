nota_atual = float(input())

maior_nota = nota_atual
menor_nota = nota_atual

while (nota_atual >= 0):
    if (nota_atual > maior_nota):
        maior_nota = nota_atual
    if (nota_atual < menor_nota):
        menor_nota = nota_atual
    nota_atual = float(input())
        
print(f"{maior_nota:.1f}")
print(f"{menor_nota:.1f}")