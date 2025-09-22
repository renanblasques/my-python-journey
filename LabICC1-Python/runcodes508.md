# Possibilidades em um jogo de damas

Uma matriz 8x8 representa a posição atual de um jogo de damas, onde:

- `0`: indica casa vazia,
- `1` indica peça branca,
- `-1` indica peça preta.

As peças pretas movem-se para frente (linhas de índice maior).

Determine as posições das peças pretas que:

- podem tomar peças brancas (captura saltando por cima de uma branca para uma casa vazia);
- podem mover-se sem tomar peças (movimento diagonal simples para uma casa vazia);
- não podem se mover.

Saída no formato:
```
Tomar: [(i, j), ...]
Mover: [...]
Parado: [...]
```

## Exemplo

### Entrada

```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 -1 0 0 0 0
0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

### Saída

```
Tomar: [(2, 3)]
Mover: []
Parado: []
```