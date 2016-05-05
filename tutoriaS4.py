#Função que fará o cálculo da média, dado uma soma de notas.
def calcularMedia(soma):
    qtdNotas = 3
    media = soma/qtdNotas

    return media

notas = [['Pedro', 4.5, 7, 9], ['Tiago', 9.4, 10, 8.6], ['Maria', 0, 5, 3.3]]

#Variável que guarda a soma das 3 notas para o cálculo da média
somaNotas = 0
#Variável que guarda o índice que representa o nome do aluno nas sublistas
indiceNome = 0
#Variável que guardará o nome do aluno ao qual iremos calcular a média
nomeAluno = ""
#For que varre a lista notas, com o objetivo de obter a média do aluno Tiago
for cont in range(len(notas)):
    #Quando cont for 1, temos o que estamos procurando.
    #Os dados do aluno Tiago estão no índice 1 da lista notas.
    if(cont == 1):
        nomeAluno = notas[cont][indiceNome]
        #For que varrerá as notas do aluno Tiago
        #Note que começamos do índice 1, pois é a partir dele que temos as notas
        for k in range(1, len(notas[cont])):
            #A linha a seguir pode ser substituída por:
            #somaNotas = somaNotas + notas[cont][k]
            somaNotas+=notas[cont][k]

media = calcularMedia(somaNotas)
#O símbolo "%.2f" % media serve para limitar o número de casas decimais a serem exibidas
#Nesse caso, foi limitado a 2 caracteres após a vírgula
print("O aluno " + nomeAluno + " possui a média igual a " + "%.2f" % media )
