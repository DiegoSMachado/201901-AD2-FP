import struct

#-----------------------------
#Leitura Padrão
def ler(entrada):
    entrada = entrada.split()
    inteiros = []
    for i in entrada:
        inteiros.append(int(i))
    return inteiros

#-----------------------------
# Memoria Principal
def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None

def selecionarMenor(vals, inicio):
    localMenor = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos]<vals[localMenor]:
            localMenor = pos
    return localMenor

def ordenarMem(valores):
    for ind in range(len(valores)):
        menor = selecionarMenor(valores, ind)
        trocar(valores, ind, menor)

def mostrarMem(valores):
    print("Ordenação da memória principal:")
    for i in valores:
        print(i, end=" ")
    print()

#-----------------------------
# Arquivo Fisico
def escreverArq(valores):
    try:
        with open("colecao.bin","wb") as arq:
            for num in valores:
                bin = struct.pack('<i', num)
                arq.write(bin)
    except IOError:
        print("Erro no arquivo")

def bubblesortArq(): #Bubble Sort feito de 2 em 2 variaveis para não alocar lista em MP
    try:
        with open("colecao.bin", 'r+b') as arq:
            arq.seek(0,2)
            totalArq = arq.tell()
            byte = struct.calcsize('<i')
            ordenado = False
            while not ordenado: #Enquanto houver x > y faça
                ordenado = True #Caso não entre no x > y ordenado é True
                contaByte = byte * 2 #Começa com 2 read()
                posicao = 0 #Define a posição do seek
                while contaByte <= totalArq: #Enquanto houver pares de 1 em 1 posição faça  Ex.: (4 3 2 1) = 4 3, 3 2, 2 1
                    arq.seek(posicao, 0)
                    x = arq.read(byte)[0]
                    y = arq.read(byte)[0]
                    if x > y: #Se não estiver ordenado
                        arq.seek(posicao,0)
                        empacotary = struct.pack('<i', y)
                        arq.write(empacotary)
                        empacotarx = struct.pack('<i', x)
                        arq.write(empacotarx)
                        ordenado = False
                    posicao += byte
                    contaByte += byte
    except IOError:
        print("Erro arquivo - Leitura")

def mostrarArq():
    try:
        with open("colecao.bin", 'rb') as arq:
            byte = struct.calcsize('<i')
            arq.seek(0,2)
            totalArq = arq.tell()
            contaByte = byte
            arq.seek(0)
            print("Ordenação do arquivo fisico")
            while contaByte <= totalArq:
                print(arq.read(byte)[0],end=" ")
                contaByte += byte
    except IOError:
        print("Erro arquivo - Leitura")

#-----------------------------
#Lendo as informações
entrada = input()
ordemMem,ordemFis = ler(entrada),ler(entrada)

#Memória Principal
ordenarMem(ordemMem)
mostrarMem(ordemMem)

#Arquivo Fisico
escreverArq(ordemFis)
bubblesortArq()
mostrarArq()