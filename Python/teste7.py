# faça uma função que peça uma lista de palavras e retorne a maior palavra.

def maior_palavra(lista):
    maior = ''
    for palavra in lista:
        if len(palavra) > len(maior):
            maior = palavra
    return maior

lista = ['otorrinolaringologista', 'terra', 'bicicleta', 'paralelepipedo', 'aviao', 'helicoptero']
print(maior_palavra(lista))

# crie uma função que conte a quantidade de caracteres do resultado da função anterior.
def contar_caracteres(palavra):
    return len(palavra)

print(contar_caracteres(maior_palavra(lista)))

print(lista[::-1]) # inverte a lista
