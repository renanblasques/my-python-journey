N = int(input())
P = int(input())

# [Leste, Sul, Oeste, Norte]
moved = [0, 0, 0, 0]

for sprint in range(2*N-1):
    direction = sprint % 4
    max_walk = N - (sprint + 1) // 2

    if P > max_walk:
        moved[direction] += max_walk
        P -= max_walk
    else:
        moved[direction] += P
        break

i = moved[1] - moved[3] + 1  # Sul - Norte + posição inicial
j = moved[0] - moved[2] + 0  # Leste - Oeste + posição inicial
center = (N//2 + 1, N//2 + 1) if N & 1 else (N//2 + 1, N//2)

# Saída
if (i, j) == center:
    print("Astronauta chegou ao centro.")
else:
    print("Astronauta não chegou ao centro.")
print(f"Posição final: ({i},{j})")
print(f"Direção final: {['Leste', 'Sul', 'Oeste', 'Norte'][direction]}")