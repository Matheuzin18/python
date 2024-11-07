'''
crie uma função que peça ao usuário uma palavra ou frase que conte quantas vezes um caractere aparece em uma string e retorne um dicionário em que as chaves são os caracteres e os valores são as quantidades de vezes que eles aparecem, considere os espaços, as letras maiúsculas e minúsculas como caracteres diferentes.
'''

def contar_caracteres(string):
    resultado = {}
    for caracter in string:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    return resultado

if __name__ == '__main__':
    string = input('Digite uma palavra ou frase: ')
    print(contar_caracteres(string))