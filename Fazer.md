# Técnicas que podemos usar

## Feature selection
- Verificar NAs
    - Eliminar se forem muito elevados
    - Tentar perceber se n da para por um valor por defeito, do tipo o mais usual ou 'unknown'

- Verificar as colunas e o número de valores diferentes
    - Caso seja demasiado elevado podemos eliminar ou tentar encontrar formas de os representar de uma forma melhor
        - A cidade pode ser com latitude e longitude (no entanto o que nos aparece são identificadore inteiros pelo que não temos como saber qual a cidade)
        - Outros podem ser por agrupar em campos menores (9 mais usuais e outros)

- Pode-se juntar alguns atributos (mas se calhar é menos usual e fácil)
- Também se pode depois aplicar um filtro de 'variance treshold' que elimina alguns atributos
- Ter sempre em atenção que alguns atributos podem só fazer sentido com outros presentes