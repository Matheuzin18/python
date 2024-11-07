'''
 crie uma função que conte quantas vezes um caractere aparece em uma string

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
print(contar_caracteres("baNaANanaA")) 