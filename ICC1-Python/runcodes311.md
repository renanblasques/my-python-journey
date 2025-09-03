# Perimetro de Poligono Regular Circunscrito

Faça um programa que receba o **numero de lados** \(N\) e o **raio da circunferencia** \(R\) de um polígono regular, e calcule o **perimetro** do polígono utilizando a fórmula:

    perimetro = 2 * N * R * sen(pi/N)

O programa deve receber os valores de entrada, calcular o perímetro e apresentar a saída.

## Entrada

A entrada consiste em duas linhas:

- Primeira linha: um número inteiro representando o número de lados \(N\).  
- Segunda linha: um número real representando o raio \(R\) da circunferência.  

## Saida

O programa deve imprimir `Perimetro: `, seguido do valor calculado (com 2 casas decimais), seguido de `unidades`.

## Exemplos

### Exemplo 1

**Entrada**
```
6
10
```

**Saida**
```
Perimetro: 60.00 unidades
```

---

### Exemplo 2

**Entrada**
```
8
5
```

**Saida**
```
Perimetro: 30.61 unidades
```

---

## Dicas de Implementacao

No Python, será necessário importar a biblioteca `math` para usar a função seno (`sin`) e o valor de `pi`.
```python
import math
```

Aqui estão algumas maneiras de formatar a saída:

### 1. Usando virgula no print
```python
perimetro = 2 * N * R * math.sin(math.pi / N)
print("Perimetro:", round(perimetro, 2), "unidades")
```

### 2. Usando `.format()`
```python
perimetro = 2 * N * R * math.sin(math.pi / N)
print("Perimetro: {:.2f} unidades".format(perimetro))
```

### 3. Usando f-string
```python
perimetro = 2 * N * R * math.sin(math.pi / N)
print(f"Perimetro: {perimetro:.2f} unidades")
```
