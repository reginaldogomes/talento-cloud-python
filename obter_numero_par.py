def obter_numero_par():
    while True:
        entrada = input("Digite um número par: ")
        
        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                return numero
            else:
                print("Você digitou um valor ímpar. Por favor, digite um número par.")
        
        except ValueError:
            print("Você digitou um caractere inválido. Por favor, digite um número par.")

numero_par = obter_numero_par()
print(f"Você digitou o número par: {numero_par}")
