# Análise aos NAs

- [**Eliminar**] PuaMode - Pua Enabled mode from the service
    - 99.97% NAs
    - tem 2309 exemplos, com 2 casos possiveis. 1 caso apenas aparece em 2 exemplos.
    - provavelmente também temos de eliminar

- [**Eliminar**] Census_ProcessorClass - A classification of processors into high/medium/low. Initially used for Pricing Level SKU. No longer maintained and updated
    - 99.59% NAs
    - provavelmente é para eliminar, tem muitos NAs e aqui até diz não é mantida!

- [**Eliminar**] DefaultBrowsersIdentifier - ID for the machine's default browser
    - 95.14% NAs
    - muitos valores diferentes (2017)
    - destes, existem 1554 com menos de 10 ocorrências
    - mas existem 155 com mais de 100
    - e 47 com mais de 1000
    - n será muito fácil tratar este, ou colocamos por classes (q n sei muito bem como)(com aquelas das mais usuais???) ou eliminamos

- [**Não Eliminar**] Census_IsFlightingInternal - NA
    - 83.04% NAs
    - apenas tem 2 classes 0 e 1.
    - existem cerca de 0.0013882241572157248% de 1s relativamente aos valores presentes!
    - logo se calhar podemos assumir que o 0 é o que é mais frequente não? apesar n sabermos o q significa tbm
    - **Por o que falta com o valor default - 0**
    
- [**Não Eliminar**] Census_InternalBatteryType - NA
    - 71.04% NAs
    - contém bastantes valores diferentes ainda (78) e alguns q apenas têm 1 ocorrência
    - mas pode ser agrupado, pq em vários casos existem carateres mal reconhecidos ou um carater diferentes que pode significar o mesmo tipo de bateria
    - **Tratar os valores**
