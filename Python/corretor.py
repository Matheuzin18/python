palavra = input("Digite uma palavra: ")
arquivo = input("Digite o nome do arquivo: ")

def criar_lista_palavras(arquivo):

    '''
    Lê um arquivo que contém uma palavra em cada linha e retorna uma lista com as palavras contidas nele.

    Parâmetros:
        arquivo (str): O nome do arquivo que contém as palavras.

    Retorna:
        list: Uma lista com as palavras contidas no arquivo.
    '''

    with open(arquivo, 'r') as arquivo:
        lista_palavras = arquivo.readlines()
    return lista_palavras

def adicionar_letra(palavra):

    '''
    Adiciona cada letra do alfabeto a todas as posições possíveis da string 'palavra' e armazena as strings resultantes em uma lista.

    Parâmetros:
        palavra (str): A palavra que será usada para criar as novas palavras.

    Retorna:
        list: Uma lista com as palavras resultantes.
    '''

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    palavras = []
    for i in range(len(palavra) + 1):
        for letra in alfabeto:
            palavras.append(palavra[:i] + letra + palavra[i:])
    return palavras


def remover_letra(palavra):
    '''
    Remove cada letra da string 'palavra' e armazena as strings resultantes em uma lista.

    Parâmetros:
        palavra (str): A palavra que será usada para criar as novas palavras.

    Retorna:
        list: Uma lista com as palavras resultantes.
    '''

    palavras = []
    for i in range(len(palavra)):
        palavras.append(palavra[:i] + palavra[i + 1:])
    return palavras

def trocar_letra(palavra):
    '''
    Troca cada letra da string 'palavra' por todas as letras do alfabeto e armazena as strings resultantes em uma lista.

    Parâmetros:
        palavra (str): A palavra que será usada para criar as novas palavras.

    Retorna:
        list: Uma lista com as palavras resultantes.
    '''

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    palavras = []
    for i in range(len(palavra)):
        for letra in alfabeto:
            palavras.append(palavra[:i] + letra + palavra[i + 1:])
    return palavras


def obter_palavras_possiveis(palavra):
    '''
    Cria uma lista com todas as palavras que podem ser obtidas a partir da palavra passada como argumento,
    utilizando as funções adicionar_letra, remover_letra e trocar_letra.

    Parâmetros:
        palavra (str): A palavra que será usada para criar as novas palavras.

    Retorna:
        list: Uma lista com as palavras possíveis.
    '''

    palavras_possiveis = []
    palavras_possiveis += adicionar_letra(palavra)
    palavras_possiveis += remover_letra(palavra)
    palavras_possiveis += trocar_letra(palavra)
    return palavras_possiveis

def verificar_palavras_corretas(palavras_possiveis, lista_palavras):
    '''
    Verifica quais palavras da lista de palavras possíveis estão contidas na lista de palavras corretas.

    Parâmetros:
        palavras_possiveis (list): Uma lista com as palavras resultantes.
        lista_palavras (list): Uma lista com as palavras que estão no arquivo.

    Retorna:
        list: Uma lista com as palavras corretas que estão contidas na lista de palavras resultantes.
    '''

    palavras_corretas = []
    for palavra in palavras_possiveis:
        if palavra in lista_palavras:
            palavras_corretas.append(palavra)
    return palavras_corretas

def sugestoes(palavra, arquivo):

    '''
    Retorna uma lista com sugestões de palavras corretas para a palavra passada como parâmetro.

    Parâmetros:
        palavra (str): A palavra que será usada para criar as novas palavras.
        arquivo (str): O nome do arquivo que contém as palavras.

    Retorna:
        list: Uma lista com sugestões de palavras corretas.
    '''

    lista_palavras = criar_lista_palavras(arquivo)
    palavras_possiveis = obter_palavras_possiveis(palavra)
    palavras_corretas = verificar_palavras_corretas(palavras_possiveis, lista_palavras)
    return palavras_corretas

print(sugestoes(palavra, arquivo))