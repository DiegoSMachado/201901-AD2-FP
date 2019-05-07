numeros = []
numero = "a"
while numero != "":
    numero = input()
    try:
        teste = float(numero)
    except ValueError:
        continue
    else:
        numeros.append(numero)
print(f"Lista de Números Válidos Lidos = {numeros}")