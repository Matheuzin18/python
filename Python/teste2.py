# crie uma função que peça ao usuário para digitar uma palavra e que retorne um dicionário contendo os caracteres da palavra e a quantidade de vezes que cada um aparece.

def contar_caracteres(string):
    resultado = {}
    for caracter in string:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    return resultado

if __name__ == '__main__':
    string = input('Digite uma palavra: ')
    print(contar_caracteres(string))
