# Esquema Conceitual para Banco De dados
Projeto criado para o Desafio prático do Bootcamp de Ciência de Dados da UNIMED - BH. A ideia é realizar o Esquema Conceitual de uma oficina, 
procurando detalhar o modelo, criando as principais entidades e suas relações.

## Oficina
O escopo inicial do projeto é voltado para a ontratação de serviços, não havendo entidades obrigatórias, mas há premissas que precisam ser seguidas para o modelo fazer
sentido. As premissas do desafio são:
- Sistema de controle e gerenciamento de execução de ordens de serviço em uma oficina mecânica
- Clientes levam veículos à oficina mecânica para serem consertados ou para passarem por revisões  periódicas
- Cada veículo é designado a uma equipe de mecânicos que identifica os serviços a serem executados e preenche uma OS com data de entrega.
- A partir da OS, calcula-se o valor de cada serviço, consultando-se uma tabela de referência de mão-de-obra
- O valor de cada peça também irá compor a OSO cliente autoriza a execução dos serviços
- A mesma equipe avalia e executa os serviços
- Os mecânicos possuem código, nome, endereço e especialidade
- Cada OS possui: n°, data de emissão, um valor, status e uma data para conclusão dos trabalhos.

## Esquema Conceitual
<p align="center"><img src="./Esquema Conceitual - Oficina.png" width="1000"></p>
