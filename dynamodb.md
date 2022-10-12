# Boas práticas com DynamoDB
## Introdução
Após todo o estudo e desafios focados em Banco de Dados Relacionais, como primeira experiência prática com Cloud Computing,
nesse desafio buscou-se apresentar alguns comandos para criar e popular tabelas NoSQL, através do DynamoDB. A importância do desafio merece ser destacada, principalmente por focar toda sua
execução no uso, conhecimento e exploração da Amazon Web Services (AWS).

Utilizando as aulas e as instruções da DIO, somada com meu interesse por arte, optei por construir uma tabela focada na "terceira arte": a pintura, onde populei-a com
informações sobre os meus artistas preferidos e suas repectivas obras.

### Serviço utilizado
- Amazon DynamoDB;
- Amazon CLI;

### Comando para criação da tabela
- Criar uma tabela
```
aws dynamodb create-table \
    --table-name Art \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=Painting,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=Painting,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
```

### Comando para popular tabela
Populando a tabela com as informações contidas nos arquivos json
- Inserir um item

```
aws dynamodb put-item \
    --table-name Art \
    --item file://itempainting.json \
```

- Inserir múltiplos itens

```
aws dynamodb batch-write-item \
    --request-items file://batchpainting.json
```
### Comando para executar consultas
Com a tabela criada e populada, é possível realizar queries simples:

- Pesquisar obras por pintores
```
aws dynamodb query \
    --table-name Art \
    --key-condition-expression "Artist = :artist" \
    --expression-attribute-values  '{":artist":{"S":"Alphonse Mucha"}}'
```

Para consultas "mais complexas", é necessário criar index secundários para que seja possível a "busca":
- Criar um index global secundário baseado no movimento artistico

```
aws dynamodb update-table \
    --table-name Art \
    --attribute-definitions AttributeName=StyleOfArt ,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"StyleOfArt-index\",\"KeySchema\":[{\"AttributeName\":\"StyleOfArt\",\"KeyType\":\"HASH\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"
```
Agora é possível executar uma consulta mais elaborada:
- Pesquisa pelo index secundário baseado no nome do artista e do movimento artístico

```
aws dynamodb query \
    --table-name Art \
    --index-name ArtistStyleOfArt-index \
    --key-condition-expression "Artist = :v_artist and StyleOfArt = :v_style" \
    --expression-attribute-values  '{":v_artist":{"S":"Alphonse Mucha"},":v_style":{"S":"Art Nouveau "} }'
```

