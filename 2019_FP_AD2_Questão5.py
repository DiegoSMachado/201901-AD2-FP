# Operação que troca o conteúdo de duas células do vetor.
def trocar(vals, posX, posY):
    temp = vals[posX]
    vals[posX] = vals[posY]
    vals[posY] = temp
    return None

# Operação que encontra e retorna o local do menor elemento do vetor,
# considerando as células a partir de um dado início.
def selecionarMenor(vals, inicio):
    localMenor = inicio
    for pos in range(inicio+1, len(vals)):
        if vals[pos]<vals[localMenor]:
            localMenor = pos
    return localMenor

# Método da Seleção
def ordenar(valores):
    for ind in range(len(valores)-1):
        menor = selecionarMenor(valores, ind)
        trocar(valores, ind, menor)
    temp = valores[0]
    valores[0] = valores[9]
    valores[9] = temp
    temp = valores[11]
    valores[11] = valores[12]
    valores[12] = temp
    return None

#Imprimi as listas ordenadas
def gravarArquivo(lista):
    try:
        with open("cartas_ordenadas.txt", "w") as arquivonovo:
            for i in range(len(cartas)):
                ordenar(cartas[i])
                for j in cartas[i]:
                    arquivonovo.write(j)
    except IOError:
        print("Erro de gravação de arquivo")

def ler(nomeArquivo):
    try:
        with open(nomeArquivo,'r') as arq:
            linhas = arq.readlines()
            for i in linhas:
                if i[len(i)-2] == "P":
                    P.append(i)
                elif i[len(i)-2] == "O":
                    O.append(i)
                elif i[len(i)-2] == "C":
                    C.append(i)
                else:
                    E.append(i)
    except IOError:
        print("Erro de leitura do arquivo")


#Lendo o arquivo
P,O,C,E = [],[],[],[]
ler("cartas.txt")
cartas = [P,O,C,E]
gravarArquivo(cartas)
print("Arquivo gerado!")