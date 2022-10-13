# Explorando Dados Demográficos com Serviços de Big Data na AWS
## Introdução
Após todo o estudo e desafios focados em Banco de Dados Relacionais, onde foram realizadas várias consultas em SQL,
agora a proposta é, utilizando as ferramentas da AWS, trabalhar com serviços de Big Data, procurando realizar consultas e gerenciar arquivos na nuvem. Para isso,
foram utilizadas ferramentas como Amazon S3 (armazenamento dos dados), Amazon Glue e Amazon Crawler (transformar os dados), para que as consultas fossem feitas no Amazon Athena,
com a visualização gráfica dos dados sendo feitas no Quicksight. A importância do desafio merece ser destacada, principalmente por focar toda sua execução no uso, conhecimento e exploração da Amazon Web Services (AWS).

## Serviços utilizados nessa atividade prática
- Amazon S3
- Amazon Glue
- Amazon Athena
- Amazon QuickSight

## Etapas para desenvolvimento
### Criar bucket no Amazon S3
- Amazon S3 Console -> Buckets -> Create bucket -> Bucket name [bootcamp_unimed] - Create bucket;
- Create folder (Criar uma pasta chamada ```/output``` e outra com o nome do seu conjunto de dados. Este nome irá definir o nome da tabela criada no Glue);
- Upload dos arquivos de dados localizados na pasta ```/population```;

### Criar Glue Crawler
- Amazon Glue Console -> Crawlers -> Add Crawler
- Source type [Data Stores] -> Crawl all folders
- Data store [S3] -> Include path [caminho do diretório dos dados de entrada]
- Create IAM Role
- Frequency [Run on demand]
- Database name [seu_nome_de_db]
- Group behavior [Create a single schema for each S3 path]
- Finish
- Databases -> Tables -> Visualizar dados das tabelas criadas

### Criar aplicação no Amazon Athena

- Query editor -> Settings -> Manage settings -> Query result location and encryption -> Browse S3 -> selecionar o bucket criado
- Selecionar Database -> criar queries (exemplos na pasta ```/src```)
- Verificar queries não salvas no bucket criado no S3
- Salvar queries -> Executar novamente -> Verificar no bucket criado no S3
- Exemplo de consulta, onde é possível ter o insight de que, mesmo a região sudeste sendo mais populosa, no nordeste temos uma maior quantidade de "regiões de saúde":
```
SELECT region,
       COUNT(health_region) AS qntd_regiao,
       SUM(population) AS population
FROM population_db.bootcamp_unimed
GROUP BY region
ORDER BY population DESC;
```

### Visualizar dados no Amazon QuickSight

- Signup (caso não tenha conta) -> Escolher [Standard]
- Datasets -> Create new dataset -> Athena -> Name [NomeDoDataSet] -> Create
- Select database -> select table -> Edit or preview -> Save & visualize
- Criar visualizações selecionando colunas, criando filtros e parâmetros e selecionando Visual types para gráficos.
