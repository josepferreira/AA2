# Análise às colunas com múltiplos valores

- [**Eliminar**] Census_OEMModelIdentifier - NA
    - 175365 valores diferentes
    - todos númericos pelo q n sei o q fazer

- [**Eliminar**] CityIdentifier - ID for the city the machine is located in
    - 107366 valores diferentes
    - grande problema é que n diz qual a cidade, mas aparece um identificador numérico pelo q n podemos usar coordenadas

- [**Eliminar**] Census_FirmwareVersionIdentifier - NA
    - 50512 valores diferentes
    - todos numéricos pelo q torna-se complicado perceber algo

- [**Eliminar**] AVProductStatesIdentifierAVProductStatesIdentifier - ID for the specific configuration of a user's antivirus software
    - 28988 valores diferentes
    - valores numéricos pelo q n sei se conseguimos extrair grande informação, nem para agrupar deve dar

- AvSigVersion - Defender state information e.g. 1.217.1014.0
    - 8531 valores distintos
    - valores do tipo X.X.X.X pelo que deve dar para agrupar por classes não?
<<<<<<< HEAD
    
    ** Nesses atributos que tem milhares de valores diferentes e são categóricos até que ponto vale a pena mante-los? Que informação relevante poderá ser dada em tantas possibilidades e cada uma com tao pouca expressividade??**
=======

- [**Eliminar**] Census_OEMNameIdentifier - NA
    - 3850 valores diferentes
    - valores inteiros do tipo X.0

- [**Eliminar**] Census_ProcessorModelIdentifier - NA
    - 3446 valores distintos
    - valores iguais ao anterior

- [**Eliminar**] DefaultBrowsersIdentifier - ID for the machine's default browser
    - 95.14% NAs
    - muitos valores diferentes (2017)
    - destes, existem 1554 com menos de 10 ocorrências
    - mas existem 155 com mais de 100
    - e 47 com mais de 1000
    - n será muito fácil tratar este, ou colocamos por classes (q n sei muito bem como)(com aquelas das mais usuais???) ou eliminamos
>>>>>>> b1febd04d2fc0b363403b487ac6eb97bd1466e89
