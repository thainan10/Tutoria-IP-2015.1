def removeValor(numeros, valor):
    retorno = []
    tamNumeros = len(numeros)
    for cont in range(tamNumeros):
        elemento = numeros[cont]

        if(elemento != valor):
            retorno.append(elemento)

    return retorno

print(removeValor([1,2,4,5,6,3,2,4,5,12,2,3,2,4,5,2], 2))
