## Análise últimas 27 variáveis

#### Pequena análise 
Estas 4 todas derivam da OSVersionFull.

As primeiras 2 têm poucos valores distintos (3 e 32, sendo que este pode mm ser diminuido se for mm nencessário penso eu). 

No entanto as últimas têm bastantes valores distintos (165 e 285) sendo todos numéricos o que torna complicada a análise. Relativamente às últimas n vejo grandes alternativas a n ser descartar ou então considerar como numérico ou mesmo categórico, mas com ordem (o q pode fazer sentido e pode n fazer).

- Census_OSArchitecture
- Census_OSBranch
- Census_OSBuildNumber
- Census_OSBuildRevision

#### Pequena análise
Apenas o último tem alguns NAs e são poucos (0.6734754748734084%).

Nenhum tem um número muito elevado de atributos(33,30,9 e 39).

O primeiro e o segundo são bastantes parecidos, sendo que podemos fazer uma melhor análise a ambos para ver as diferenças e se vale a pena mantermos os 2. Para além disso caso seja necessário penso que dá para encurtar o número de valores possíveis agrupando por classes.

O último são apenas valores numéricos pelo q n é muito simples conseguir algum tipo de clustering. Temos de verificar se faz sentido estar presente, até pq n tem um número de valores distintos exagerado.

- Census_OSEdition
- Census_OSSkuName 
- Census_OSInstallTypeName 
- Census_OSInstallLanguageIdentifier

#### Pequena análise