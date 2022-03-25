
from time import sleep
from random import randrange

def main():
    print('_' * 35)
    print('         GERADOR DE SENHAS         ')
    print('_' * 35)

    print('Com quantos caracteres gostaria que tivesse sua senha?')
    solicitação = int(input('Escolher opção: '))

    password = []

    for c in range(0, solicitação):
        arquivo = open("caracteres.txt", "r")
        caracteres = []
        for linha in arquivo:
            linha = linha.strip()
            caracteres.append(linha)
        arquivo.close

        numero = randrange(0, len(caracteres))
        caractere_aleatorio = caracteres[numero]
        password.append(caractere_aleatorio)

    sleep(1)
    print('Gerando uma senha...')
    sleep(1)
    print('\033[1;31mA senha foi gerada, não se esqueça de anota-lá!')
    print(''.join(password))

if __name__ == "__main__":
    main()