sair = 0
#Lista que guardará todos os pacientes.
#Cada paciente é uma sublista da lista pacientes.
pacientes = []
while(sair != 1):
    #Recebendo os dados dos pacientes e guardando na lista pacientes.
    nomeCri = str.upper(input("Informe o nome da criança: "))
    nomePai = str.upper(input("Informe o nome do pai: "))
    nomeMae = str.upper(input("Informe o nome da mãe: "))
    idade = int(input("Informe a idade da criança: "))

    paciente = [nomeCri, nomePai, nomeMae, idade]
    pacientes.append(paciente)

    sair = int(input("Deseja sair? Caso sim, digite 1, caso não digite 0: "))

def gravaPacientes(nomeArq, pacientes):
    #Abrindo o arquivo em modo de escrita.
    arquivo = open(nomeArq, 'w')

    tamPacientes = len(pacientes)

    #Varrendo a lista de pacientes.
    for cont in range(tamPacientes):
        paciente = pacientes[cont]
        tamPaciente = len(paciente)

        #Varrendo e salvando os dados de cada paciente.
        for k in range(tamPaciente):
            #Transformando o dado em str para poder ser gravado no arquivo.
            dado = str(paciente[k])
            #Testando se k é o último índice da lista.
            #Caso seja, o dado é adicionado sem a vírgula no fim.
            if(k == tamPaciente - 1):
                arquivo.write(dado)
            else:
                arquivo.write(dado + ',')
        #Inserindo as quebras de linhas entre os pacientes.
        arquivo.write("\n")
gravaPacientes("pacientes.txt", pacientes)

def getPacientes(nomeArq):
    #Abrindo o arquivo em modo de leitura.
    arquivo = open(nomeArq, 'r')
    linhas = arquivo.readlines()
    tamLinhas = len(linhas)

    #Lista que será retornada.
    pacientes = []

    for cont in range(tamLinhas):
        linha = linhas[cont]
        """Criando a lista com os dados de cada paciente.
        A função split() quebra o texto de acordo com o
        caractere passado como parâmetro. """
        dadosPaciente = linha.split(',')
        pacientes.append(dadosPaciente)
    return pacientes

getPacientes("pacientes.txt")

def listarPacientes(nomeArq):
    pacientes = getPacientes(nomeArq)
    tamPacientes = len(pacientes)
    indiceNomePaciente = 0

    for cont in range(tamPacientes):
        print(pacientes[cont][indiceNomePaciente])
listarPacientes("pacientes.txt")
