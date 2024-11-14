def ano_nascimento(idade, ano_atual):
    '''
    Uma função que recebe a idade e o ano atual de uma pessoa e calcula o seu ano de nascimento.

    Parâmetros:
        idade (int): A idade da pessoa.
        ano_atual (int): O ano atual.
    
    Retorno:
        int: O ano de nascimento da pessoa.
    '''
    return ano_atual - idade

# Testando a função
print(ano_nascimento(17, 2024)) # 2007