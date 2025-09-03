# Três Seis Consecutivos

Faça um programa que simule o lançamento de um dado. O programa deve ler uma sequência de números inteiros representando os resultados dos lançamentos até que três números `6` consecutivos sejam obtidos.

O programa deve contar o número total de lançamentos necessários para atingir esse objetivo. Além disso, o programa deve validar a entrada, garantindo que apenas números entre 1 e 6 sejam considerados como lançamentos válidos.

## Entrada

A entrada consiste em uma sequência de números inteiros, um por linha.

## Saída

O programa deve imprimir:

- A mensagem `Numero invalido! Digite um numero entre 1 e 6.` para cada número de entrada que não esteja no intervalo de 1 a 6.
- Ao final, quando três números `6` consecutivos forem lidos, o programa deve imprimir a mensagem `Voce conseguiu 3 seis consecutivos em {X} lancamentos!`, onde `{X}` é o número total de lançamentos válidos.

## Exemplo

### Entrada
```
1
2
6
1
6
6
8
6
```

### Saída
```
Numero invalido! Digite um numero entre 1 e 6.
Numero invalido! Digite um numero entre 1 e 6.
Voce conseguiu 3 seis consecutivos em 7 lancamentos!
```