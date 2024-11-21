'''
crie uma função que retorne a maior palavra da lista

se mais de uma palavra for a maior, retorna a primeira delas
'''

def maior_palavra(lista):
    maior = ''
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

import doctest
doctest.testmod(verbose=True)