# Projeto Lógico de Banco de Dados

## Introdução ao problema

Projeto criado para o Desafio prático do Bootcamp de Ciência de Dados da UNIMED - BH. 
A ideia é realizar o projeto lógico de um e-commerce, procurando detalhar e refinar o modelo, criando todas as entidades e suas relações, 
indicando suas respectivas primary keys e foreign keys. Após isso, construir queries complexas com as tabelas criadas;

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

## Projeto Lógico
```
-- Projeto Lógico de Banco de Dados - Criação do Banco de Dados para o Cenário de E-commerce

-- Criando Database
CREATE DATABASE ecommerce;
USE ecommerce;

-- Criando tabelas
-- Cliente
CREATE TABLE Cliente (
	id_cliente INT NOT NULL PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    identificacao_cpf CHAR(11),
    identificacao_cnpj CHAR(14),
    Endereço VARCHAR(30) NOT NULL,
    CEP CHAR(8) NOT NULL
    );

-- Frete
CREATE TABLE Frete (
	id_frete INT NOT NULL PRIMARY KEY,
    CEP CHAR(8) NOT NULL,
    Endereço VARCHAR(30) NOT NULL,
    valor FLOAT NOT NULL
    );
    
-- Pedido
CREATE TABLE Pedido (
	id_pedido INT NOT NULL PRIMARY KEY,
    categoria VARCHAR(45),
    Endereço VARCHAR(30),
    id_cliente INT,
    status_pedido VARCHAR(45),
    id_vendedor INT
    );
    
-- Entrega
CREATE TABLE Entrega (
	id_entrega INT NOT NULL PRIMARY KEY,
    razao_social VARCHAR(45),
    nome_da_empresa VARCHAR(45),
	data_envio DATE,
    data_entrega DATE,
    status_entrega VARCHAR(45),
    constraint fk_entrega_pedido foreign key (id_pedido) references Pedido(id_pedido),
    constraint fk_entrega_cliente foreign key (id_cliente) references Cliente(id_cliente),
    constraint fk_entrega_frete foreign key (id_frete) references Frete(id_frete)
    );
    
-- Produto
CREATE TABLE Produto (
	id_produto INT NOT NULL PRIMARY KEY,
    categoria VARCHAR(45),
    descricao VARCHAR(45),
	valor FLOAT, 
    desconto FLOAT,
    constraint fk_estoque_produto foreign key (id_estoque) references Estoque(id_estoque),
    constraint fk_fornecedor_produto foreign key (id_fornecedor) references Fornecedor(id_fornecedor)
    );

-- Fornecedor
CREATE TABLE Fornecedor (
	id_fornecedor INT NOT NULL PRIMARY KEY,
    razao_social VARCHAR(45),
    cnpj CHAR(14),
	valor FLOAT, 
    desconto FLOAT,
    constraint fk_estoque_produto foreign key (id_estoque) references Estoque(id_estoque),
    constraint fk_fornecedor_produto foreign key (id_fornecedor) references Fornecedor(id_fornecedor)
    );

-- Vendedor - Terceiro
CREATE TABLE vendedor_terceiro (
	id_vendedor INT NOT NULL PRIMARY KEY,
    razao_social VARCHAR(45),
    cnpj CHAR(14)
    );

-- Estoque
CREATE TABLE Estoque (
	id_estoque INT NOT NULL PRIMARY KEY,
    id_produto INT,
    estoque INT,
    id_vendedor INT 
    );
    
-- Campanha promocional
CREATE TABLE Campanha (
	id_campanha INT NOT NULL PRIMARY KEY,
	nome_campanha VARCHAR(45),
    data_inicio DATE,
    data_termino DATE
);

CREATE TABLE Produto_campanha (
	id_produto INT NOT NULL PRIMARY KEY,
    categoria VARCHAR(45),
    descricao VARCHAR(45),
	valor FLOAT, 
    desconto FLOAT,
    constraint fk_produto_campanha foreign key (id_campanha) references Campanha(id_campanha)
    );
```

## Queries
```
-- Exercício 1
-- Encontre para mim todos os pedidos que estão com status de 'shipped', pode trazer todas as informações
SELECT *
FROM pedidos ped 
WHERE id_pedidos IN (
	SELECT id_pedidos
	FROM entrega
	WHERE status_entrega = 'shipped')

-- Exercício 2
-- Monte um relatório de todos os produtos cadastrados que tem preço de venda acima da média
SELECT *
FROM produtos p
WHERE id_produto IN (
	SELECT id_produto
	FROM pedido ped
	WHERE ped.valor > (
		SELECT AVG(p.valor)
		FROM produto p))

-- Exercício 3
-- Informações dos vendedores que venderam produtos da categoria 'cama_mesa_banho'
SELECT *
FROM vendedores_terceiro vt 
WHERE id_vendedor IN (
	SELECT id_vendedor
	FROM pedido ped 
	WHERE id_produto IN (
		SELECT id_produto
		FROM produto p 
		WHERE categoria = 'cama_mesa_banho'))
```

