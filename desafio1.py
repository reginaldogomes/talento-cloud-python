# Executando o código
nota = 10
resultado1 = nota <= 10

nota = 6
faltas = 4
resultado2 = (nota <= 6) and (faltas <= 3)

convidados = 3
fumante = False
resultado3 = (convidados > 4) or (fumante == True)

dia = "qua"
resultado4 = (dia == "sab") or (dia == "dom")

feriado = True
resultado5 = not(feriado == False)

dia = "ter"
feriado = False
resultado6 = (dia == "seg") or not(feriado == False)

# Exibindo os resultados
print(f"Resultado do Exercício 1: {resultado1}")  # True
print(f"Resultado do Exercício 2: {resultado2}")  # False
print(f"Resultado do Exercício 3: {resultado3}")  # False
print(f"Resultado do Exercício 4: {resultado4}")  # False
print(f"Resultado do Exercício 5: {resultado5}")  # True
print(f"Resultado do Exercício 6: {resultado6}")  # False