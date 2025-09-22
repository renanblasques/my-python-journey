# Contagem de elementos na matriz

Faça um programa que:

- Leia os valores de uma matriz 4x5 de inteiros;
- Leia 2 inteiros (A e B), sendo A < B;
- Conte quantos valores da matriz estão dentro do intervalo [A, B].

## Exemplo

### Entrada

```
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
5 15
```

### Saída

```
11
```

## Dica de Implementação

- Para ler dois números inteiros na mesma linha e armazenar em duas variáveis diferentes (chamadas de A e B), utilize:
```
A, B = map(int, input().split())
```