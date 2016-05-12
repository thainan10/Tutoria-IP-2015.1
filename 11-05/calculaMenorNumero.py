quantidadeNumeros = 5

#Recebe o primeiro número.
menorNumero = int(input("Informe um número:"))

#Recebe os demais números.
for cont in range(quantidadeNumeros - 1):
    numero = int(input("Informe um número:"))

    #Se o número recebido for menor que o menor número atual, atualiza o valor.
    if(numero < menorNumero):
        menorNumero = numero

print("O menor número informado é: ", menorNumero)
