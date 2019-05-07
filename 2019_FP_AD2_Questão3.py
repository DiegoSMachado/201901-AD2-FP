#Lendo o arquivo
def lista(nomeArquivo):
    try:
        with open(nomeArquivo,'r') as arq:
            lista = arq.read().split()
            return lista
    except IOError:
        print("Error ao abrir o arquivo")

def conjunto(caracter):
    conjunto = set()
    for i in palavra:
        conjunto.add(i)
    return conjunto

def verificar(lista,conjunto):
    dicionario = dict()
    qtConjunto = len(conjunto)
    qtLista = len(lista)
    palavrasChaves = []
    i = 0
    print(f"Listagem do dicionário das palavras contendo {conjunto}:")
    while i < qtLista:
        caracter = 0
        for j in conjunto:
            if lista[i].find(j) != -1:
                caracter += 1
        if qtConjunto == caracter:
            if dicionario.get(lista[i]) == None:
                dicionario[lista[i]] = 1
                palavrasChaves.append(lista[i])
            else:
                dicionario[lista[i]] += 1
        i+=1
    palavrasChaves.sort()
    for i in range(len(palavrasChaves)):
        print(f"{palavrasChaves[i]} ocorreu {dicionario[palavrasChaves[i]]} vez")

nomeArquivo = input()
palavra = input()
lista = lista(nomeArquivo)
conjunto = conjunto(palavra)
verificar(lista,conjunto)