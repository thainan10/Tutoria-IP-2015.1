#Lista que irá receber o nome e a idade dos clientes, sempre nessa ordem.
clientes = []

sair = "N"
while (sair != "S"):
    nome = input("Informe o nome do cliente: ")
    idade = int(input("Informe a idade do cliente: "))

    clientes.append(nome)
    clientes.append(idade)

    sair = nome

tamClientes = len(clientes)
clientesAcimaDe30 = []

#Laço que varre apenas números ímpares, ou seja, os índices das idades.
for cont in range(1, tamClientes, 2):
    #Testa se a idade dos clientes é maior que 30.
    #Se for, adiciona o nome e depois a idade na lista "clientesAcimaDe30".
    if(clientes[cont] > 30):
        clientesAcimaDe30.append(clientes[cont-1])
        clientesAcimaDe30.append(clientes[cont])

tamClientesAcimaDe30 = len(clientesAcimaDe30)

#Testa: Se a lista "clientesAcimaDe30" for vazia, não há clientes com idade maior que 30.
if(tamClientesAcimaDe30 == 0):
    print("Nenhum cliente tem mais de 30 anos")
else:
    #Varre a lista "clientesAcimaDe30", mostrando o nome e a idade desses clientes
    for cont in range(0, tamClientesAcimaDe30, 2):
        print("Cliente: ", clientesAcimaDe30[cont], ", com idade: ", clientesAcimaDe30[cont+1], ".")
