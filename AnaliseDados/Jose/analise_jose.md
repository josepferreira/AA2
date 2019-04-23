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

Nenhum dos seguintes 4 tem NAs.

O primeiro contém bastantes valores distintos (147). Como são todos ids e são numéricos n existe muito que fazer para os tratar, e nem a descrição da variável ajuda, pq n existe.

Os restantes têm um número razoável de valores distintos (6,2,5).

- Census_OSUILocaleIdentifier 
- Census_OSWUAutoUpdateOptionsName 
- Census_IsPortableOperatingSystem 
- Census_GenuineStateName 

#### Pequena análise
Primeira e última não têm NAs. Census_IsFlightingInternal tem 83.044030% e Census_IsFlightsDisabled tem 1.799286% de NAs.

O primeiro tem 6 valores diferentes, mas caso seja mesmo necessário dá para agrupar em 3 talvez.
O último tem 10 valores diferentes, caso seja necessário podemos tentar ver uma forma de os agrupar. Pelo que estive a ver na net podem existir alguns valores q n fazem sentido, mas n tenho certezas.

Os restantes têm 2 valores possíveis (0 ou 1), no entanto o 1 aparece muitas poucas vezes (menos de 0.01%) pelo q podemos assumir q nos restantes (os NAs) aparecem com a classe 0.


- Census_ActivationChannel
- Census_IsFlightingInternal
- Census_IsFlightsDisabled
- Census_FlightRing


#### Pequena análise

O último não contém NAs, os restantes contém a seguinte percentagem: 63.524472, 2.054109, 1.794915.

O primeiro tem 2 valores possíveis (0 e 1) e o 1 apenas aparece em cerca de 0.02% dos casos, pelo q podemos tratar os NAs colocando a 0. O último também tem apenas 2 valores possíveis.

O segundo tem 712 valores diferentes e tudo numérico (identificadores) pelo q n sei o q podemos fazer.
O terceiro tem 50494 valores diferentes e tudo numérico (identificadores) pelo q podemos eliminar.

- Census_ThresholdOptIn
- Census_FirmwareManufacturerIdentifier
- Census_FirmwareVersionIdentifier
- Census_IsSecureBootEnabled

#### Pequena análise

Os dois primeiros têm 63.439038% e 0.178816% de valores nulos, respetivamente. Os restantes n têm NAs.

Todos têm apenas 2 valores diferentes (0 e 1).

1. Quanto aos NAs:
    - o primeiro apenas tem 0.000031% de 1s pelo q podemos preencher com 0s (aparece apenas 1 caso com 1 pelo q pode até ser outlier ou n significativo)
    - o segundo tem 0.703945% de 1s pelo q me parece q tbm podemos preencher com 0s


- Census_IsWIMBootEnabled
- Census_IsVirtualDevice
- Census_IsTouchEnabled
- Census_IsPenCapable

#### Pequena análise

1. As percentagens de valores nulos são as seguintes:
    - 0.799676
    - 3.401352
    - 3.401352

Os dois primeiros têm 2 valores diferentes (0 e 1). O terceiro tem 15 valores diferentes, numéricos que identificam a região. Provavelmente será a melhor maneira de representar a zona (visto q é a mais abrangente e com menos valores possíveis).

2. Relativamente aos NAs:
    - o primeiro tem 5.74192% de 1s pelo q n será tão linear quantos os anteriores
    - o segundo tem 28.357855% de 1s pelo q se calhar vai ser preciso prever estes valores n?
    - o terceiro tem muitas classes distintas sem haver grande destaque pelo q podemos fazer uma 'unknown' ou 'other'


- Census_IsAlwaysOnAlwaysConnectedCapable
- Wdft_IsGamer
- Wdft_RegionIdentifier