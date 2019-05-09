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
# Funções da Memoria Principal
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
# Funções Arquivo Fisico
def escreverArq(valores):
    try:
        with open("colecao.bin","wb") as arq:
            for num in valores:
                arq.write(struct.pack('=i', num)) #popula o arquivo com a lib struct
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
                ordenado = True #Caso não entre no Se x > y
                contaByte = byte * 2 #Começa com 2 read()
                posicao = 0 #Define a posição do seek
                while contaByte <= totalArq: #Enquanto houver pares de 1 em 1 posição faça  Ex.: (4 3 2 1) = 4 3, 3 2, 2 1
                    arq.seek(posicao, 0) #Volta na posição de inicio de while
                    x = struct.unpack("=i",arq.read(byte))[0] #le 1 inteiro
                    y = struct.unpack("=i",arq.read(byte))[0] #le 2 inteiro
                    if x > y: #Se não estiver ordenado
                        arq.seek(posicao,0) #Volte a posição inicial
                        arq.write(struct.pack('=i', y)) #troca x por y
                        arq.write(struct.pack('=i', x)) #troca y por x
                        ordenado = False #defina como não ordenado
                    posicao += byte #Conta a posição
                    contaByte += byte #Conta ate o fim do byte
    except IOError:
        print("Erro arquivo - Leitura")

def mostrarArq():
    try:
        with open("colecao.bin", 'rb') as arq:
            byte = struct.calcsize('=i') #recebe o tamanho do byte gasto
            arq.seek(0,2) #coloca a posição no final do arquivo
            totalArq = arq.tell() #recebe o qts byte tem no final do arquivo
            contaByte = byte #contador recebe primeiro byte
            arq.seek(0) #volta a posição pro inicio do arquivo
            print("Ordenação do arquivo fisico:")
            while contaByte <= totalArq:
                print(struct.unpack("=i",arq.read(byte))[0],end=" ")
                contaByte += byte #conta ate o fim do byte
    except IOError:
        print("Erro arquivo - Leitura")

#-----------------------------
#Lendo as informações
entrada = input()
ordemMem,ordemFis = ler(entrada),ler(entrada) #Lê como inteiro numa lista

#Memória Principal
ordenarMem(ordemMem) #Ordena na memória
mostrarMem(ordemMem) #Lista resultado da memória

#Arquivo Fisico
escreverArq(ordemFis) #Escreve colecao.bin com as informações
bubblesortArq() #Ordena de 2 em 2 o Arquivo
mostrarArq() #Lista o resultado do Arquivo
