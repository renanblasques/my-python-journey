# Lista de Compras

Fernando é dono de um pequeno mercado de bairro. Todos os dias ele precisa controlar os produtos que entram nas prateleiras, os preços de cada item e, no final do dia, calcular quanto ele vendeu no total. Até agora ele fazia isso no papel, mas a pilha de notas está ficando gigante e confusa.

Ele te contratou como programador para criar um programa em Python que ajude a organizar suas compras e cálculos de forma automatizada.

Seu programa deve:

- Perguntar ao usuário quantos produtos deseja cadastrar.
- Para cada produto, receber:
    - O nome do produto
    - O preço do produto
    - Armazenar os produtos e preços em um dicionário.

Ao final do cadastro, o programa deve:

- Exibir a lista completa de produtos e preços;
- Calcular o total da compra;
- Calcular a média dos preços;
- Identificar o produto mais caro e o mais barato (usando uma função).
- Permitir que o usuário digite o nome de um produto e verificar se ele está na lista.
    - Se estiver, mostrar seu preço;
    - Caso contrário, informar que não foi encontrado.

## Exemplo

### Entrada

```
3
Arroz
25.50
Feijao
8.90
Oleo
6.80
Feijao
```

### Saída

```
Lista de compras:
- Arroz: R$ 25.50
- Feijao: R$ 8.90
- Oleo: R$ 6.80

Total da compra: R$ 41.20
Media de precos: R$ 13.73
Mais caro: Arroz (R$ 25.50)
Mais barato: Oleo (R$ 6.80)

Produto encontrado: Feijao custa R$ 8.90
```