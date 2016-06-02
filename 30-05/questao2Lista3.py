def calculaEstacionamento(tipoVeic, horasPerm, minsPerm):
    #Taxa até 5h
    taxaFixa = 3
    #Taxa a mais por hora ou fração de hora
    taxaExcedente = 2

    #Guarda o tempo de permanência total em minutos
    tempoPerm = (horasPerm * 60) + minsPerm

    #Valor total a ser pago
    valorTotal = 0

    if (horasPerm < 5):
        valorTotal = taxaFixa
    else:
        valorTotal+=taxaFixa
        tempoPerm-=300

        while(tempoPerm >= 60):
            valorTotal+=taxaExcedente
            tempoPerm-=60
        if(tempoPerm != 0):
            valorTotal+=taxaExcedente
            tempoPerm = 0

    tipoVeic = str.upper(tipoVeic)
    if(tipoVeic == "CARRO"):
        return valorTotal
    elif(tipoVeic == "MOTO"):
        valorTotal/=2
        return valorTotal
    else:
        #Retorna -1 se o tipo informado for inválido
        return -1
print(calculaEstacionamento("carro", 5, 1))
