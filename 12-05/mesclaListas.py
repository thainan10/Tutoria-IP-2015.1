lista1 = [1,2,3,4]

lista2 = [4,2,5,6,2,1]

#Lista que mescla as listas "lista1" e "lista2".
listaGeral = lista1 + lista2

#Transforma a lista em um set.
#Set é uma estrutura que não permite elementos repetidos.
listaGeral = set(listaGeral)

#Transforma o set "listaGeral" em uma lista novamente.
listaGeral = list(listaGeral)

print(listaGeral)
