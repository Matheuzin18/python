'''
crie uma função que conte quantas vezes um caractere aparece em uma string e retorne um dicionário em que as chaves são os caracteres e os valores são as quantidades de vezes que eles aparecem, considere os espaços, as letras maiúsculas e minúsculas como caracteres diferentes.
'''

def contar_caracteres(string):
    resultado = {}
    for caracter in string:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    return resultado

# Exemplo de uso
print(contar_caracteres("BatATA quenTinHa"))
