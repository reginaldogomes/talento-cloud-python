def calcular(num1: int, num2: int, operacao: int) -> int:
    if operacao == 1:
        return somar(num1, num2)
    elif operacao == 2:
        return subtrair(num1, num2)
    elif operacao == 3:
        return multiplicar(num1, num2)
    elif operacao == 4:
        return dividir(num1, num2)
    else:
        return operacao_invalida()

def somar(a: int, b: int) -> int:
    return a + b

def subtrair(a: int, b: int) -> int:
    return a - b

def multiplicar(a: int, b: int) -> int:
    return a * b

def dividir(a: int, b: int) -> int:
    if b == 0:
        print("Erro: Divisão por zero não permitida.")
        return 0
    return a // b  # Divisão inteira

def operacao_invalida() -> int:
    print("Erro: Operação inválida.")
    return 0

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = int(input("Digite a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))
    
    resultado = calcular(num1, num2, operacao)

    if resultado is not None:
      operacao_str = {
          1: "Soma",
          2: "Subtração",
          3: "Multiplicação",
          4: "Divisão"
      }.get(operacao, "Operação Inválida")

    print(f"Resultado da {operacao_str}: {resultado}")

if __name__ == "__main__":
    main()
