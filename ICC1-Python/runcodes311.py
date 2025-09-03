import math

N = int(input())
R = float(input())

perimetro = 2 * N * R * math.sin(math.pi / N)

print(f"Perimetro: {perimetro:.2f} unidades")
