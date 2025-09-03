# Peso Ideal

Faça um programa que receba a **altura** e o **sexo** de uma pessoa, calcule e imprima o seu peso ideal utilizando as fórmulas:

- **Para homens:**  
  `(72.7 × Altura) - 58`
- **Para mulheres:**  
  `(62.1 × Altura) - 44.7`

O programa deve receber os valores de entrada, calcular o peso ideal e apresentar a saída.


## Entrada

A entrada consiste em duas linhas:

- Primeira linha: um número real representando a altura em metros.  
- Segunda linha: uma letra (`M` para masculino, `F` para feminino).  


## Saída

O programa deve imprimir `Peso ideal: `, seguido do valor calculado (com 2 casas decimais), seguido de `kg`, utilizando o formato de impressão de preferência.


## Exemplos

### Exemplo 1

**Entrada**
```
1.80
M
```

**Saída**
```
Peso ideal: 72.86 kg
```

---

### Exemplo 2

**Entrada**
```
1.65
F
```

**Saída**
```
Peso ideal: 57.77 kg
```

---

## Dicas de Implementação

No Python, existem várias maneiras de formatar a saída no `print`. Aqui estão três exemplos:

### 1. Usando vírgula no print
###### Obs: Para esse caso, você deve arredondar o número antes de imprimir, utilizando a função round().
```python
print("Peso ideal:", round(peso_ideal, 2), "kg")
```

### 2. Usando `.format()`
```python
print("Peso ideal: {:.2f} kg".format(peso_ideal))
```

### 3. Usando f-string
```python
print(f"Peso ideal: {peso_ideal:.2f} kg")
```