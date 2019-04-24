**[Categórico]** O atributo *PuaMode* possui muitos valores missing (99.98%) e apenas apresenta 1 valor distinto ("on") pelo que será melhor excluir este atributo.

**[Categórico]** O atributo *SMode* possui relativamente poucos valores missing (6.02%) e apresenta 2 valores distintos ("0" e "1"). Neste atributo podemos substituir os missing por "0" dado que 94% das entradas apresentam este valor. Além disso, este atributo indica se o computador apenas pode instalar aplicações da Microsoft Apps sendo que por default não se verifica.

**[Categórico]** O atributo *IeVerIdentifier* possui poucos valores missing (0.66%) e apresenta 189 valores distintos (não existindo relações entre eles). Este atributo não possui qualquer descrição pelo que o grupo não consegue identificar a que se refere. Pode ser possível considerar apenas os 50 mais frequentes e agrupar os restantes numa classe "Others".

**[Categórico]** O atributo *SmartScreen* possui alguns valores missing (35.61%) e apresenta 13 valores distintos. Aqui talvez podemos assumir que os missing correspondem ao computador não possuir smartscreen. Podemos também agrupar os valores "on" e "On" num só valor - "On" - e os valores "off", "Off" e "OFF" num só valor - "Off".

**[Categórico]** O atributo *Firewall* possui poucos valores missing (1.03%) e apresenta 2 valores distintos ("0" e "1"). 
**QUAL SERÁ A MELHOR ABORDAGEM PARA LIDAR COM OS NaN?**
- Assumir que os valores em falta podem ser interpretados como "1"(firewall ativa) dada a criticidade de ignorar os "0"(firewall inativa).
- Assumir que como o serviço não reportou firewall ativa então é porque ela não está ativa.

**[Categórico]** O atributo *UacLuaenable* possui muito poucos valores missing (0.12%) e apresenta 7 valores distintos. Este atributo deveria apenas possuir uma gama de valores "0" ou "1" (ativo ou inativo) pelo que alguns dos exemplos contém alguns erros (valores superiores a "1"). O mais natural aqui será considerar que todos os valores superiores a "1" correspondem ao valor "1" e que os valores missing correspondem também ao valor "1" dado este valor aparecer em mais de 99% dos exemplos

**[Categórico]** O atributo *Census_MDC2FormFactor* não possui valores nulos e apresenta 12 valores distintos. Não parece ser necessário efetuar alterações aos valores deste atributo.

**[Categórico]** O atributo *Census_DeviceFamily* não possui valores nulos e apresenta 3 valores distintos, sendo que um deles visível em mais de 99.8% dos exemplos ("Windows.Desktop") e outro visível em apenas 2 exemplos ("Windows"). Não parece ser necessário efetuar alterações aos valores deste atributo. Apenas se pode agrupar os valores "Windows.Desktop" e "Windows" num só valor - "Windows.Desktop" mas não parece ser necessário.

**[Categórico]** O atributo *Census_OEMNameIdentifier* possui poucos valores missing (1.07%) e apresenta 1664 valores distintos (não existindo relações entre eles). Este atributo não possui qualquer descrição pelo que o grupo não consegue identificar a que se refere. Pode ser possível considerar apenas os 50 mais frequentes e agrupar os restantes numa classe "Others".

**[Categórico]** O atributo *Census_OEMNameIdentifier* possui poucos valores missing (1.15%) e apresenta 45095 valores distintos (não existindo relações entre eles). Este atributo não possui qualquer descrição pelo que o grupo não consegue identificar a que se refere. Pode ser possível considerar apenas os 50 mais frequentes e agrupar os restantes numa classe "Others". A melhor opção talvez seja remover este atributo devido ao elevado número de valores distintos.

**[Discreto]** O atributo *Census_ProcessorCoreCount* possui muito poucos valores missing (0.48%) e apresenta 28 valores distintos. A melhor solução aqui é talvez substituir os missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_ProcessorManufacturerIdentifier* possui muito poucos valores missing (0.48%) e apresenta 4 valores distintos. A melhor solução aqui é talvez substituir os missing pelo valor mais frequente.

**[Categórico]** O atributo *Census_ProcessorModelIdentifier* possui muito poucos valores missing (0.48%) e apresenta 2331 valores distintos (não sendo possível agrupá-los). A melhor solução aqui é talvez remover este atributo assumindo que os modelos se podem agrupar pelo seu fabricante (atributo anterior - "Census_ProcessorManufacturerIdentifier").

**[Categórico]** O atributo *PuaMode* possui muitos valores missing (99.59%) e apresenta 3 valor distintos. Não parece haver uma forma correta de retirar uma quantidade tão elevada de valores missing. Além disso, este atributo parece possuir uma correlação muito elevada com o atributo "Census_ProcessorCoreCount" pelo que será melhor excluir este atributo.



