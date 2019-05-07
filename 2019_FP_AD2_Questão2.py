#Operação que troca o conteúdo de duas células do vetor.
def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None

# Operação que encontra e retorna o local do menor elemento do vetor,
# considerando as células a partir de um dado início.
def selecionarMenor(vals, inicio, posicao):
    localMenor = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos][posicao]<vals[localMenor][posicao]:
            localMenor = pos
    return localMenor

#Método da Seleção
def ordenar(valores, posicao):
    for ind in range(len(valores)-1):
        menor = selecionarMenor(valores, ind, posicao)
        trocar(valores, ind, menor)
    return None

#Lendo o arquivo
def ler(nomeArquivo):
    try:
        with open(nomeArquivo,'r') as arq:
            arquivo = arq.readlines()
            lista = []
            if arquivo == []:
                print(f"{nomeArquivo} está vazio!!!")
                return False
            else:
                print(f"----- Listagem dos Produtos Lida do Arquivo: {nomeArquivo} -----")
                for linha in arquivo:
                    linhaSeparada = linha.split()
                    tupla = (str(linhaSeparada[0]),int(linhaSeparada[1]),float(linhaSeparada[2]))
                    lista.append(tupla)
                    print(tupla)
                return lista
    except IOError:
        print("Erro ao abrir o arquivo!")

#Imprimi as listas ordenadas
def lista(lista):
    for elemento in lista:
        print(elemento)

#Rodando o programa
nomeArquivo = input()
resultado = ler(nomeArquivo)
i=0
if resultado != False:
    while i < 3:
        print("----------------------------------------------------------------------")
        print(f"----- Listagem dos Produtos Ordenados Pelo Campo: {i+1} -----")
        ordenar(resultado,i)
        lista(resultado)
        i += 1