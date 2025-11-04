texto = input()

nomes = texto.split()

iguais = []

for nome in nomes:
    if nomes.count(nome) > 1:
        iguais.append(nome)

print(iguais)