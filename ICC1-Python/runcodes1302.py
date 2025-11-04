nome_completo = input()

iniciais = []

for palavra in nome_completo.split():
    inicial = palavra[0].upper()
    iniciais.append(inicial)

print(iniciais)