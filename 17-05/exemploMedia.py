"""Função que recebe uma lista de números como parâmetro
e retorna a média deles."""
def calculaMedia(numeros):
    tamNumeros = len(numeros)
    soma = 0
    #Laço que irá realizar a soma dos números da lista.
    for cont in range(tamNumeros):
        soma+=numeros[cont]

    media = soma / tamNumeros
    return media

"""Receber 3 números do usuário, calcular a média deles através
da função "calculaMedia" e exibi-la ao usuário."""

#Variável que guarda a quantidade de números que serão pedidos.
qtdNumeros = 3
#Lista que guardará os números inforamados.
numeros = []
for cont in range(qtdNumeros):
    num = float(input("Informe um número para o cálculo da média: "))
    numeros.append(num)

#Variável que guarda o valor da média retornado pela função.
media = calculaMedia(numeros)

print("A média dos números informados é: ", media)
