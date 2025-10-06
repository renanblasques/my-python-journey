resistant_sequence = input().strip().upper()
virus_sequence = input().strip().upper()

occurrences = virus_sequence.count(resistant_sequence)

if virus_sequence.find("U") != -1:
    virus_type = "RNA"
else:
    virus_type = "DNA"

if occurrences == 0:
    resistance = "Nao resistente"
elif occurrences == 1:
    resistance = "Resistente"
elif occurrences == 2:
    resistance = "Muito resistente"
else:
    resistance = "Super resistente"

print("INFORMACOES DO VIRUS")
print(f"Tipo: {virus_type}")
print(f"Resistencia: {resistance}")
print(f"Numero de ocorrencias: {occurrences}")
