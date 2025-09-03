competition = input().strip()

if competition == 'P':
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    d = [d1, d2, d3]
    d.sort()
    print(f"Melhor marca: {d[-1]:.1f}")
elif competition == 'D':
    dist = float(input())
    time = float(input())
    pace = time / (dist / 1000)
    print(f"Pace: {pace:.2f} min/km")
else:
    print("Entrada invalida")