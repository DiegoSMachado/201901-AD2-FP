numeros = []
numero = "a" #recebe "a" para passar pelo while
while numero != "":
    numero = input()
    try:
        teste = float(numero) #testa a capacidade de tornar um número
    except ValueError:
        continue #Se não for possivel ignora
    else:
        numeros.append(numero) #caso contrario recebe a string na lista
print(f"Lista de Números Válidos Lidos = {numeros}")