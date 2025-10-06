n = int(input())
tempo_total = 0
tempos = []

for _ in range(n):
    time = int(input())
    tempos.append(time)

tempo_anterior = tempos[0]

for i in range(1, n):
    tempo_atual = tempos[i]
    if (tempo_atual - tempo_anterior > 10):
        tempo_total = tempo_total + 10
    else:
        tempo_total = tempo_total + (tempo_atual - tempo_anterior)
    tempo_anterior = tempos[i]

tempo_total = tempo_total + 10

print(tempo_total)