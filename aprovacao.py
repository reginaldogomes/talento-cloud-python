# Função para determinar o status do aluno
def verificar_status(nota):
    if nota < 4:
        return "Reprovado"
    elif nota < 7:
        return "Em recuperação"
    else:
        return "Aprovado"

# Solicita a nota do aluno
try:
    nota = float(input("Digite a nota do aluno: "))

    # Verifica o status com base na nota
    status = verificar_status(nota)
    print(f"O status do aluno é: {status}")
except ValueError:
    print("Por favor, digite um valor numérico válido para a nota.")
