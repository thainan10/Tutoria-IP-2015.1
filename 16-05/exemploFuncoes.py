numeros = []
num = int(input("Informe um número e, caso deseje sair, informe o valor -1: "))
numeros.append(num)

while(num != -1):
    num = int(input("Informe um número e, caso deseje sair, informe o valor -1: "))
    numeros.append(num)

def calculaMedia(numeros):
    soma = 0
    tamNumeros = len(numeros)

    for cont in range(tamNumeros):
        soma+=numeros[cont]

    media = soma/tamNumeros
    return media

def calculaMenorNumero(numeros):
    menorNumero = 0
    tamNumeros = len(numeros)

    for cont in range(tamNumeros):
        numero = numeros[cont]
        if(numero < menorNumero):
            menorNumero = numero

    return menorNumero

def salvaHtml(numeros, nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    tamNumeros = len(numeros)

    arquivo.write("<h1 style='color:red'>Números da lista:</h1>")
    
    for cont in range(tamNumeros):
        texto = "<p style='margin-right:10px'>" + str(numeros[cont]) + "</p>"
        arquivo.write(texto)

    media = calculaMedia(numeros)
    texto = "<h2>A média desses números é igual a: " + str(media) + "</h2>"
    arquivo.write(texto)

    menorNumero = calculaMenorNumero(numeros)
    texto = "<h2>O menor desses números é: " + str(menorNumero) + ".</h2>"
    arquivo.write(texto)
    
salvaHtml(numeros, "testeNumeros.html")
    
