#Abre o arquivo e o armazena na variável "arquivo".
arquivo = open("teste.txt", 'w')
quantidade = 3

#Recebe os nomes e as idades dos usuários.
for cont in range(quantidade):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    """
    Salva os dados recebidos o arquivo.
    Essa função só aceita argumentos String.
    O caractere especial "\n" serve para quebrar a linha no String.
    A função "str()" transforma a idade de inteiro pra String.
    """
    arquivo.write("O nome do cliente é: " + nome + "\n")
    arquivo.write("A idade do cliente é: " + str(idade) + "\n")

#Fecha o arquivo.
arquivo.close()
