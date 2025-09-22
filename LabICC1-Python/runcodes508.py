D = []
for i in range(8):
    linha = list(map(int, input().split()))
    while len(linha) < 8:
        linha += list(map(int, input().split()))
    D.append(linha[:8])

tomar, mover, parado = [], [], []

for i in range(8):
    for j in range(8):
        if D[i][j] == -1:
            can_capture = False
            can_move = False
            # captura para esquerda
            if i + 2 < 8 and j - 2 >= 0:
                if D[i+1][j-1] == 1 and D[i+2][j-2] == 0:
                    can_capture = True
            # captura para direita
            if i + 2 < 8 and j + 2 < 8:
                if D[i+1][j+1] == 1 and D[i+2][j+2] == 0:
                    can_capture = True
            # movimento simples
            if i + 1 < 8 and j - 1 >= 0 and D[i+1][j-1] == 0:
                can_move = True
            if i + 1 < 8 and j + 1 < 8 and D[i+1][j+1] == 0:
                can_move = True

            if can_capture:
                tomar.append((i, j))
            elif can_move:
                mover.append((i, j))
            else:
                parado.append((i, j))

print("Tomar:", tomar)
print("Mover:", mover)
print("Parado:", parado)
