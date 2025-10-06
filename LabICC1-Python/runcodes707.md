# Painel de LEDs

João quer montar um painel de LEDs com vários números. Como é desejável que haja o menor desperdício, faça um algoritmo que o informe quantos filamentos é necessário para montar um painel, considerando uma margem de 5 LEDs acima.

![Foto dos LEDs](https://resources.beecrowd.com/gallery/images/problems/UOJ_1168.png)

Utilize um dicionário para armazenar a quantidade de LEDs necessária para cada dígito dos número digitado.

## Regras de entrada

A entrada contém um inteiro `N`, correspondente ao número de casos de teste, seguido de `N` linhas.

## Saída

Para cada caso de teste, imprima a quantidade de LEDs necessária para que João monte o painel apresentado. Não se esqueça de incluir os 5 LEDs reservas.


## Exemplo

### Entrada

```
3
115380
2819311
23456
```

### Saída

```
32 leds
34 leds
30 leds
```