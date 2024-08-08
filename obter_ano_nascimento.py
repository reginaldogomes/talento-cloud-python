def obter_ano_nascimento():
    while True:
        entrada = input("Digite o ano de nascimento (entre 1922 e 2021): ")
        
        try:
            ano_nascimento = int(entrada)
            
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano inválido. O ano deve estar entre 1922 e 2021.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o ano.")

def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento

nome = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()
ano_atual = 2022
idade = calcular_idade(ano_nascimento, ano_atual)

print(f"{nome}, você completou ou completará {idade} anos em {ano_atual}.")