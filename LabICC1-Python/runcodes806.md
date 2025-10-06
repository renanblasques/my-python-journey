# Operações com Numpy

Alberto é engenheiro de produção e precisa analisar a produtividade de diferentes linhas de montagem de uma fábrica. Ele recebe, todo dia, uma matriz com os números de peças produzidas por linhas (linhas da matriz) e turnos (colunas da matriz). Como ele não é muito bom com cálculos, contratou você para programar um programa em Python que utilize `numpy` para ajudá-lo.

Escreva um programa em Python que:

- Leia dois inteiros n e m, representando respectivamente o número de linhas de produção e o número de turnos.
- Leia uma matriz n x m de números inteiros representando a quantidade de peças produzidas.
- Calcule e mostre:
    - A matriz original.
    - A soma total de peças produzidas.
    - A média geral de peças.
    - A soma de cada linha (produção por linha de montagem).
    - A soma de cada coluna (produção por turno).
    - O maior valor da matriz (produção máxima em um turno específico).

O menor valor da matriz (produção mínima em um turno específico).

## Exemplo

### Entrada

```
3 4
10 20 15 30
5  25 20 10
12 18 22 28
```

### Saída

```
Matriz de producao:
[[10 20 15 30]
 [ 5 25 20 10]
 [12 18 22 28]]

Soma total: 215
Media geral: 17.92
Soma por linha: [75 60 80]
Soma por turno: [27 63 57 68]
Maior valor: 30
Menor valor: 5
```