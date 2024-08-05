# Usando o Laço for
def imprimir_andares_for():
    for andar in range(20, 0, -1):  # Começa em 20 e vai até 1
        if andar != 13:
            print(andar)

imprimir_andares_for()

# Usando o Laço while
def imprimir_andares_while():
    andar = 20
    while andar > 0:
        if andar != 13:
            print(andar)
        andar -= 1

imprimir_andares_while()

# Usando o Laço do-while Simulado com while
def imprimir_andares_do_while():
    andar = 20
    while True:
        if andar != 13:
            print(andar)
        andar -= 1
        if andar == 0:
            break

imprimir_andares_do_while()


