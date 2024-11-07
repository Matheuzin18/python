'''
crie uma funçaõ que conte quantas vezes cada caracter aparece em uma string
exemplo: batata
b: 1
a: 3
t: 2 
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
print(contar_caracteres("paralelogramo"))