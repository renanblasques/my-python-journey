
## Equação do 2º Grau

Você deve criar um programa que resolva **equações do 2º grau** da forma:

$
ax^2 + bx + c = 0
$

O programa recebe como entrada os valores dos coeficientes **a**, **b** e **c** (números reais) e deve calcular as raízes da equação usando a **fórmula de Bhaskara**.

O cálculo deve seguir as seguintes regras:  

Calcule o discriminante (**Δ**):
  \[
  \Delta = b^2 - 4ac
  \]
- **Se Δ > 0** → duas raízes reais e diferentes.  
- **Se Δ = 0** → uma raiz real (raiz dupla).  
- **Se Δ < 0** → não existem raízes reais (exibir mensagem correspondente).  

### Entrada
A entrada consiste em **3 linhas**, cada uma contendo um número real, representando respectivamente os valores de **a**, **b** e **c**.

### Saída
O programa deve imprimir:  
- As duas raízes reais, caso **Δ > 0**.  
- A raiz única, caso **Δ = 0**.  
- A frase `"Nao existem raizes reais"` caso **Δ < 0**.

---

### Exemplos

**Exemplo 1**

Entrada:
```
1
-3
2
```

Saída:
```
2.0 1.0
```

---

**Exemplo 2**

Entrada:
```
1
-2
1
```

Saída:
```
1.0
```

---

**Exemplo 3**

Entrada:
```
1
0
4
```

Saída:
```
Nao existem raizes reais
```
---
### Dicas de Implementação

- Leia os coeficientes **a**, **b** e **c** usando `input()` e converta-os para `float` → `float(input())`.  
- Calcule o **delta** usando a fórmula: `delta = b**2 - 4*a*c`.
- Use a biblioteca `math`. Na primeira linha do programa, digite:
```
import math
```
- Essa biblioteca possui função `sqrt()` para calcular a raiz quadrada de um número. 
```
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)
```