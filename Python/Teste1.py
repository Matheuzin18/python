# crie uma função que conte quantas vezes cada caractere aparece em uma string. Ela deve receber uma string e retornar um dicionário onde as chaves são os caracteres e os valores são o número de vezes que cada um aparece.

def contar_caracteres(string):
    resultado = {}
    for caracter in string:
        if caracter in resultado:
            resultado[caracter] += 1
        else:
            resultado[caracter] = 1
    return resultado

# Exemplo de uso
print(contar_caracteres("bola de golfe"))  