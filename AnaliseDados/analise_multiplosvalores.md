# Análise às colunas com múltiplos valores

- Census_OEMModelIdentifier - NA
    - 175365 valores diferentes
    - todos númericos pelo q n sei o q fazer

- CityIdentifier - ID for the city the machine is located in
    - 107366 valores diferentes
    - grande problema é que n diz qual a cidade, mas aparece um identificador numérico pelo q n podemos usar coordenadas

- Census_FirmwareVersionIdentifier - NA
    - 50512 valores diferentes
    - todos numéricos pelo q torna-se complicado perceber algo

- AVProductStatesIdentifierAVProductStatesIdentifier - ID for the specific configuration of a user's antivirus software
    - 28988 valores diferentes
    - valores numéricos pelo q n sei se conseguimos extrair grande informação, nem para agrupar deve dar

- AvSigVersion - Defender state information e.g. 1.217.1014.0
    - 8531 valores distintos
    - valores do tipo X.X.X.X pelo que deve dar para agrupar por classes não?
    
    ** Nesses atributos que tem milhares de valores diferentes e são categóricos até que ponto vale a pena mante-los? Que informação relevante poderá ser dada em tantas possibilidades e cada uma com tao pouca expressividade??**