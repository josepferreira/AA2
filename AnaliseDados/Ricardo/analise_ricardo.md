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

**[Categórico]** O atributo *Census_OEMModelIdentifier* possui poucos valores missing (1.15%) e apresenta 45095 valores distintos (não existindo relações entre eles). Este atributo não possui qualquer descrição pelo que o grupo não consegue identificar a que se refere. Pode ser possível considerar apenas os 50 mais frequentes e agrupar os restantes numa classe "Others". A melhor opção talvez seja remover este atributo devido ao elevado número de valores distintos.

**[Discreto]** O atributo *Census_ProcessorCoreCount* possui muito poucos valores missing (0.48%) e apresenta 28 valores distintos. A melhor solução aqui é talvez substituir os missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_ProcessorManufacturerIdentifier* possui muito poucos valores missing (0.48%) e apresenta 4 valores distintos. A melhor solução aqui é talvez substituir os missing pelo valor mais frequente.

**[Categórico]** O atributo *Census_ProcessorModelIdentifier* possui muito poucos valores missing (0.48%) e apresenta 2331 valores distintos (não sendo possível agrupá-los). A melhor solução aqui é talvez remover este atributo assumindo que os modelos se podem agrupar pelo seu fabricante (atributo anterior - "Census_ProcessorManufacturerIdentifier").

**[Categórico]** O atributo *Census_ProcessorClass* possui muitos valores missing (99.59%) e apresenta 3 valor distintos. Não parece haver uma forma correta de retirar uma quantidade tão elevada de valores missing. Além disso, este atributo parece possuir uma correlação muito elevada com o atributo "Census_ProcessorCoreCount" pelo que será melhor excluir este atributo.

**[Discreto]** O atributo *Census_PrimaryDiskTotalCapacity* possui muito poucos valores missing (0.62%) e apresenta 1194 valores distintos. Pode-se substituir os valores missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_PrimaryDiskTypeName* possui muito poucos valores missing (0.15%) e apresenta 4 valores distintos. Talvez seja possível juntar os valores "UNKNOWN" e "Unspecified" num só valor - "Unspecified". Pode-se também substituir os valores missing pelo valor mais frequente - "HDD".

**[Discreto]** O atributo *Census_SystemVolumeTotalCapacity* possui muito poucos valores missing (0.62%) e apresenta 158820 valores distintos. Pode-se substituir os valores missing pela média dos restantes valores. Parece apresentar algumas semelhanças com o atributo *Census_PrimaryDiskTotalCapacity*.

**[Categórico]** O atributo *Census_HasOpticalDiskDrive* não possui valores missing e apresenta 2 valor distintos. Não é necessário modificar este atributo.

**[Discreto]** O atributo *Census_TotalPhysicalRAM * possui muito poucos valores missing (0.94%) e apresenta 626 valores distintos. Pode-se substituir os valores missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_ChassisTypeName* possui muito poucos valores missing (0.01%) e apresenta 35 valor distintos. Parece ser uma versão mais detalhada do atributo "Census_MDC2FormFactor". **Qual dos dois utilizar? Talvez utilizar os dois? Talvez o Census_ChassisTypeName seja demasiado específico?** Acho que podemos usar só o "Census_MDC2FormFactor".

**[Discreto]** O atributo *Census_InternalPrimaryDiagonalDisplaySizeInInches* possui muito poucos valores missing (0.54%) e apresenta 508 valores distintos. Por ser discreto não é necessário efetuar alterações a este atributo. Pode-se substituir os valores missing pela média dos restantes valores.

**[Discreto]** O atributo *Census_InternalPrimaryDisplayResolutionHorizontal* possui muito poucos valores missing (0.54%) e apresenta 539 valores distintos. Por ser discreto não é necessário efetuar alterações a este atributo.Pode-se substituir os valores missing pela média dos restantes valores.

**[Discreto]** O atributo *Census_InternalPrimaryDisplayResolutionVertical* possui muito poucos valores missing (0.54%) e apresenta 569 valores distintos. Por ser discreto não é necessário efetuar alterações a este atributo.Pode-se substituir os valores missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_ChassisTypeName* possui muito poucos valores missing (0.001%) e apresenta 9 valor distintos. Parece ter uma elevada relação com os atributos "Census_MDC2FormFactor" e "Census_ChassisTypeName". É possível substituir os valores missing pelo valor mais frequente - "Mobile".

**[Categórico]** O atributo *Census_InternalBatteryType* possui muitos valores missing (71.05%) e apresenta 30 valor distintos. Talvez agrupar todos os valores começados por "li" e assumir que os valores missing podem ser representados por "li"?
**ACABAR**

**[Discreto]** O atributo *Census_InternalBatteryNumberOfCharges* possui poucos valores missing (3.04%) e apresenta 5947 valores distintos. Por ser discreto não é necessário efetuar alterações a este atributo. Pode-se substituir os valores missing pela média dos restantes valores.

**[Categórico]** O atributo *Census_OSVersion* não possui valores missing e apresenta 304 valores distintos. Pode-se agrupar as várias versões reduzindo o número de valores distintos.




