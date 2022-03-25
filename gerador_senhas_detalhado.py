
from time import sleep
from random import randrange

def main():
    # imprime a apresentação do gerador de senhas
    print('_' * 35)
    print('         GERADOR DE SENHAS         ')
    print('_' * 35)


    print('Com quantos caracteres gostaria que tivesse sua senha?')
    solicitação = int(input('Escolher opção: ')) # na variavel "solicitação" recebr o valor de texto(string) atravez do
    # input que e convertida em um numero intero atraves do int()
    password = [] # lista para adicionar os caracteres da senha

    # repetição que começão em 0 e vai ate a quantidade de vezes infomada pela solicitação
    for c in range(0, solicitação):
        arquivo = open("caracteres.txt", "r") # a variavel arquivo abre o orquivo caracteres.txt em modo de leitura
        caracteres = [] # lista para adicionar os caracteres da senha para a contagem
        for linha in arquivo: # for linha in arquivo -> para cada linha do arquivo
            linha = linha.strip() # remove os espaços e \n dos caracteres
            caracteres.append(linha) # adiciona em caracteres atravez do .append
        arquivo.close # fecha o arquivo

        numero = randrange(0, len(caracteres)) # na variavel numero faz a contagem de caracteres dentro da lista
        # caracteres atravez do len()
        caractere_aleatorio = caracteres[numero]
        password.append(caractere_aleatorio) # adiciona os caracteres na lista password

    sleep(1) # espera 1s
    print('Gerando uma senha...')
    sleep(1) # espera 1s
    print('\033[1;31mA senha foi gerada, não se esqueça de anota-lá!') # exibe uma mensagem vermelha atravez do \033[1;31mA
    print(''.join(password)) # e exibida a lista password sem os separadores '',

if __name__ == "__main__":
    main()