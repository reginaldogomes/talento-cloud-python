def determinar_categoria(rodas, peso, pessoas):
    if rodas == 2 or rodas == 3:
        return "A"
    elif rodas == 4:
        if pessoas <= 8:
            if peso <= 3500:
                return "B"
            elif 3500 < peso <= 6000:
                return "C"
        elif pessoas > 8:
            return "D"
    if rodas >= 4:
        if peso > 6000:
            return "E"
        elif 3500 < peso <= 6000:
            return "C"
        elif pessoas > 8:
            return "D"
    return "Categoria não encontrada"

# Solicita as características do veículo
try:
    rodas = int(input("Digite a quantidade de rodas do veículo: "))
    peso = float(input("Digite o peso bruto do veículo em quilogramas: "))
    pessoas = int(input("Digite a quantidade de pessoas no veículo: "))

    # Determina a categoria de habilitação
    categoria = determinar_categoria(rodas, peso, pessoas)
    print(f"A melhor categoria de habilitação para o veículo informado é: {categoria}")
except ValueError:
    print("Por favor, insira valores válidos para as características do veículo.")
