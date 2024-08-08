def calcular(num1: int, num2: int, operacao: int) -> int:
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero não permitida.")
            return None
        return num1 // num2  # Usando divisão inteira
    else:
        print("Erro: Operação inválida.")
        return None

def exibir_menu():
    print("\nEscolha uma operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

while True:
    exibir_menu()
    
    try:
        operacao = int(input("Digite o número da operação: "))
        
        if operacao == 0:
            print("Saindo do programa.")
            break
        
        if operacao not in [1, 2, 3, 4]:
            print("Essa opção não existe")
            continue

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        resultado = calcular(num1, num2, operacao)
        
        if resultado is not None:
            operacao_str = {
                1: "Soma",
                2: "Subtração",
                3: "Multiplicação",
                4: "Divisão"
            }.get(operacao, "Operação Inválida")
            
            print(f"Resultado da {operacao_str}: {resultado}")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
