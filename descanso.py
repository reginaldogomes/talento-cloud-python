import time

def descanso():
    print("Iniciando o descanso")
    tempo_descanso = 45  # tempo de descanso em segundos
    for segundo in range(1, tempo_descanso + 1):
        print(f"{segundo} segundos")
        time.sleep(1)
    print("O tempo de descanso terminou! Volte ao exercício.")

# Chamando a função de descanso
descanso()
