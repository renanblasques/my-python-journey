# Vírus Resistente

Dr. Henrique está realizando pesquisas com vírus e descobriu que alguns trechos de DNA aparecem repetidamente em diferentes amostras. Ele percebeu que a quantidade de vezes em que o trecho resistente aparece no DNA ou RNA da bactéria pode indicar o nível de resistência.

Seu trabalho é escrever um programa que analise o trecho genético, classifique o vírus em tipo (RNA ou DNA) e nível de resistência:

- Tipo do vírus
    - *DNA* -> contém as bases nitrogenadas `A`,`T`,`C` e `G`
    - *RNA* -> contém as bases nitrogenadas `A`,`U`,`C` e `G`

- Resistência do vírus
    - *Não resistente* → quando o trecho resistente não aparece no DNA.
    - *Resistente* → quando o trecho resistente aparece exatamente uma vez.
    - *Muito resistente* → quando o trecho resistente aparece duas vezes.
    - *Super resistente* → quando o trecho resistente aparece três ou mais vezes.

## Regras de entrada

A entrada consiste em duas linhas:

- A primeira linha contém a sequência de código genético que representa o trecho resistente.
- A segunda linha contém a sequência genética do vírus a ser analisada.

As strings são compostas apenas pelos caracteres: `A`,`T`,`C`,`G` e `U` (maiúsculos ou minúsculos!).

## Saída

Imprima as informações do vírus:
```
INFORMACOES DO VIRUS
Tipo: tipo
Resistencia: classificacao
Numero de ocorrencias: n
```

## Exemplo

### Entrada

```
cgt
ACGTCGTAGTCGTACGTCGTACGT
```

### Saída

```
INFORMACOES DO VIRUS
Tipo: DNA
Resistencia: Super resistente
Numero de ocorrencias: 6
```