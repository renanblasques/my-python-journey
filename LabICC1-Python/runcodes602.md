# Registro de Notas dos Alunos

Imagine que você é o professor de uma turma e precisa organizar as notas dos alunos. 

Você quer descobrir quem está se destacando e qual é a maior média da turma. Para isso, você deve criar um programa em Python que ajuda a controlar as notas de forma simples.

O programa lê o nome e três notas de cada aluno e armazena em uma  matriz, permitindo:

- mostrar todas as notas registradas,
- calcular a média de cada aluno,
- identificar o aluno com a maior média.


## Regras de entrada

- Cada linha contém:  

```
NOME NOTA1 NOTA2 NOTA3
```

- `NOME` é uma string (sem espaços).  
- `NOTA1`, `NOTA2` e `NOTA3` são números reais.  
- Para encerrar a entrada, digite:  

```
-1
```

## Saída

O programa mostra:

- A matriz de dados (nome + notas de cada aluno)  
- O aluno com a maior média e o valor dessa média, com duas casas decimais

Formato do resultado:

```
Matriz de notas:
[[NOME NOTA1 NOTA2 NOTA3]
 [NOME NOTA1 NOTA2 NOTA3]
 ... ]

Maior média: VALOR (NOME)
```

---

## Exemplo

### Entrada

```
Clara 8 7 9
Ana 6 10 8
José 10 9 8
-1
```

### Saída

```
Matriz de dados:
[['Clara' '8.0' '7.0' '9.0']
 ['Ana' '6.0' '10.0' '8.0']
 ['José' '10.0' '9.0' '8.0']]

Maior média: 9.00 (José)
```


## Dicas de Implementação

- Crie uma matriz completa que será utilizada para imprimir na tela;
- Crie uma outra matriz contendo apenas as notas. Utilize para isso:
```
matriz_notas = matriz_original[:, 1:].astype(float)
```
Obs: O `astype(float)` converte os valores da matriz para o tipo `float`;
- Crie um vetor de médias com `np.mean`;
- Obtenha o índice do maior elemento do vetor com `np.argmax`.