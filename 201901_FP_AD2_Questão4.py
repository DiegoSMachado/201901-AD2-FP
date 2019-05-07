import struct

def trocarMem(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None

def selecionarMenorMem(vals, inicio):
    localMenor = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos]<vals[localMenor]:
            localMenor = pos
    return localMenor

def ordenarMem(valores):
    for ind in range(len(valores)):
        menor = selecionarMenorMem(valores, ind)
        trocarMem(valores, ind, menor)

def lerMem(entrada):
    entrada = entrada.split()
    inteiros = []
    for i in entrada:
        inteiros.append(int(i))
    return inteiros

def escreverFis(valores):
    try:
        with open("colecao.bin","wb") as arq:
            bin = bytearray(valores)
            arq.write(bin)
    except IOError:
        print("Erro no arquivo")

def teste():
    ordenado = False
    try:
        with open("colecao.bin", 'rb') as arq:
            arq.seek(0,2)
            quantidade = arq.tell()
    except IOError:
        print("Erro arquivo - Leitura")

    while not ordenado:
        ordenado = True
        for i in range(quantidade-1):
            try:
                with open("colecao.bin", 'rb') as arq:
                    arq.seek(i,0)
                    posx = arq.read()
                    arq.seek(i+1,0)
                    posy = arq.read()
            except IOError:
                print("Erro arquivo - Leitura")
            if posx > posy:
                try:
                    with open("colecao.bin", 'wb') as arq:
                        arq.seek(i,0)
                        arq.write(posy)
                        arq.seek(i+1,0)
                        arq.write(posx)
                        ordenado = False
                except IOError:
                    print("Erro arquivo - Gravação")
    try:
        with open("colecao.bin", 'rb') as arq:
            for i in range(quantidade-1):
                arq.seek(i)
                print(arq.read()[0], end=" ")
            print()
    except IOError:
        print("Erro ao abrir o arquivo")


def mostrar(valores):
    for i in valores:
        print(i, end=" ")
    print()

#Lendo as informações
entrada = input()
ordemMem = lerMem(entrada)
ordemFis = lerMem(entrada)

#Memória Principal
ordenarMem(ordemMem)
print("Ordenação da memória principal:")
mostrar(ordemMem)

#Arquivo Fisico
escreverFis(ordemFis)
teste()