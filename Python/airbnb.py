import csv

def ler_dados_csv(nome_arquivo):

    '''
    Lê os dados do arquivo csv e retorna um DataFrame que contem as informações dos anúncios.

    Os dados são separados em:
    'id': Identificação do anúncio.
    'neighbourhood': Bairro onde a acomodação está localizada.
    'price': Preço por noite, em dólar.
    'name': Título do anúncio.
    '''

    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = [linha for linha in leitor]
    return dados


def contar_anuncios(dados):

    '''
    Recebe a lista de anúncios e retorna o número total de anúncios.
    '''

    return len(dados)


def bairro_mais_anuncios(dados):

    '''
    Recebe a lista de anúncios e retorna o bairro com o maior número de anúncios.
    '''

    bairros = {}
    for anuncio in dados:
        if anuncio['neighbourhood'] in bairros:
            bairros[anuncio['neighbourhood']] += 1
        else:
            bairros[anuncio['neighbourhood']] = 1
    return max(bairros, key=bairros.get)


def calcular_preco_medio(dados):

    '''
    Recebe a lista de anúncios e retorna o preço médio das acomodações.
    '''

    total_preco = 0
    for anuncio in dados:
        total_preco += float(anuncio['price'])
    return total_preco / len(dados)


def anuncio_mais_caro(dados):

    '''
    Recebe a lista de anúncios e retorna um dicionário com todas as informações do anúncio com o preço mais alto.
    '''

    return max(dados, key=lambda x: float(x['price']))


def bairro_menor_e_maior_preco_media(dados):

    '''
    Recebe a lista de anúncios e o o bairro com a maior média de preço, o bairro com a menor média de preço e os valores das médias. 
    '''

    bairros = {}
    for anuncio in dados:
        if anuncio['neighbourhood'] in bairros:
            bairros[anuncio['neighbourhood']].append(float(anuncio['price']))
        else:
            bairros[anuncio['neighbourhood']] = [float(anuncio['price'])]
    bairros_media = {bairro: sum(preco) / len(preco) for bairro, preco in bairros.items()}
    bairro_menor_preco = min(bairros_media, key=bairros_media.get)
    bairro_maior_preco = max(bairros_media, key=bairros_media.get)
    return bairro_menor_preco, bairros_media[bairro_menor_preco], bairro_maior_preco, bairros_media[bairro_maior_preco]



def gerar_relatorio_airbnb (nome_arquivo):

    '''
    Utiliza as funções anteriores para gerar um relatório com as seguintes informações sobre os anúncios do Airbnb:
    Número total de anúncios.
    Bairro com o maior número de anúncios.
    Preço médio das acomodações.
    Anúncio com o preço mais alto.
    Bairro com a maior média de preço.
    Bairro com a menor média de preço.

        Parametros:
            nome_arquivo (str) : nome do arquivo csv de onde os dados serão lidos

        Retorna:
            relatorio (str) : string com as informações obtidas dos anuncios do Airbnb
    '''

    dados = ler_dados_csv(nome_arquivo)
    relatorio = f'Número total de anúncios: {contar_anuncios(dados)}\n'
    relatorio += f'Bairro com o maior número de anúncios: {bairro_mais_anuncios(dados)}\n'
    relatorio += f'Preço médio das acomodações: {calcular_preco_medio(dados)}\n'
    anuncio = anuncio_mais_caro(dados)
    relatorio += f'Anúncio com o preço mais alto: {anuncio["name"]} - {anuncio["price"]}\n'
    bairro_menor_preco, menor_preco, bairro_maior_preco, maior_preco = bairro_menor_e_maior_preco_media(dados)
    relatorio += f'Bairro com a maior média de preço: {bairro_maior_preco} - {maior_preco}\n'
    relatorio += f'Bairro com a menor média de preço: {bairro_menor_preco} - {menor_preco}\n'
    return relatorio

print(gerar_relatorio_airbnb('airbnb.csv'))

# Número total de anúncios: 100
# Bairro com o maior número de anúncios: Copacabana
# Preço médio das acomodações: 306.0
# Anúncio com o preço mais alto: Casa 3 quartos com piscina - 1000
# Bairro com a maior média de preço: Leblon - 400.0
# Bairro com a menor média de preço: Botafogo - 200.0
