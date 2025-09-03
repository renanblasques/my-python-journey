# Inversão de Número

Faça um programa que leia um número inteiro positivo de três dígitos e gere outro número formado pelos dígitos invertidos do número lido.

## Entrada

A entrada consiste em uma única linha contendo um número inteiro positivo com três dígitos.

## Saída

O programa deve imprimir o número invertido, mantendo os possíveis zeros à esquerda.

## Exemplos

### Exemplo 1

**Entrada**
```
123
```

**Saída**
```
321
```

---

### Exemplo 2

**Entrada**
```
500
```

**Saída**
```
005
```

---

## Dicas de Implementação

Em Python, você pode inverter os dígitos de um número:

### 1. Usando operações matemáticas
```python
n = int(input())
centena = n // 100
dezena = (n % 100) // 10
unidade = n % 10
invertido = unidade * 100 + dezena * 10 + centena
print(invertido)
```

### 2. Usando strings (geral)
```python
n = input()
print(n[::-1])
```
