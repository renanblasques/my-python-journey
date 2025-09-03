collecting_data = True
collected_count = 0
ph_list = []

while collecting_data:
    ph = float(input())
    if ph == -1.0:
        break
    if 0.0 <= ph <= 14.0:
        collected_count += 1
        ph_list.append(ph)

if collected_count > 0:
    min_ph = min(ph_list)
    max_ph = max(ph_list)
    avg_ph = sum(ph_list) / collected_count

    print(f"Numero de coletas validas: {collected_count}")
    print(f"pH maximo: {max_ph:.1f}")
    print(f"pH minimo: {min_ph:.1f}")
    print(f"pH medio: {avg_ph:.1f}")
else:
    print("Nenhum dado valido foi coletado.")