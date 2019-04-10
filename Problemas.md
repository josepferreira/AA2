## Problemas

- Como o ficheiro é muito grande vamos ter de trabalhar por chunks
- Para visualizar os missing values em gráfico temos o problema de nem com 1 milhão dar (com 400k dá no mínimo)

#### Para criar um ficheiro com as primeiras X entradas basta fazer:
###### head -X train.csv | tee train_X.csv