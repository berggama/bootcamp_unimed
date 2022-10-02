# Projeto Conceitual de Banco de Dados
Projeto criado para o Desafio prático do Bootcamp de Ciência de Dados da UNIMED - BH. A ideia é realizar o Modelo Conceitual de um e-commerce, procurando detalhar
e refinar o modelo, criando todas as entidades e suas relações, indicando suas respectivas primary keys e foreign keys.

## E-commerce
O escopo inicial do projeto é voltado para a venda de produtos, tendo que, obrigatoriamente, possuir as entidades Produto, Estoque, Cliente, Pedido e Fornecedor, ficando
aberta a possibildiade de acrescentar qualquer outra entidade que ache necessário.
As premissas do desafio são:

### Produto
- Os produtos são vendidos por uma única plataforma online. Contudo, estes podem
ter vendedores distintos (terceiros)
- Cada produto possui um fornecedor
- Um ou mais produtos podem compor um pedido

### Cliente
- O cliente pode se cadastrar no site com seu CPF ou CNPJ
- O endereço do cliente irá determinar o valor do frete
- Um cliente pode comprar mais de um pedido. Este tem um período de carência para devolução do produto

### Pedido
- O pedido são criados por clientes e possuem informações de compra, endereço e status da entrega
- Um produto ou mais compoem o pedido
- O pedido pode ser cancelado

## Modelo Conceitual
<p align="center"><img src="./Projeto Conceitual de Banco de Dados – E-COMMERCE.png" width="1000"></p>
