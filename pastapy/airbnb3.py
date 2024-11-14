import csv

def ler_arquivo(airbnb):
    '''
    Lê os dados do arquivo csv e retorna uma lista de dicionários com as informações dos anúncios.

    os dados são separados em:
    'id': Identificação do anúncio.
    'neighbourhood': Bairro onde a acomodação está localizada.
    'price': Preço por noite, em dólar.
    'name': Título do anúncio.
    '''

    with open(airbnb, 'r') as file:
        reader = csv.DictReader(file)
        data = [line for line in reader]
    return data


def contar_anuncios(data):
    '''
    Recebe a lista com os anúncios e retorna o número total de anúncios.
    '''

    return len(data)

def bairro_mais_anuncios(data):
    ''''
    Recebe a lista de anúncios e retorna o nome do bairro com o maior número de anúncios.
    '''

    bairros = {}
    for anuncio in data:
        if anuncio['neighbourhood'] in bairros:
            bairros[anuncio['neighbourhood']] += 1
        else:
            bairros[anuncio['neighbourhood']] = 1
    return max(bairros, key=bairros.get)


def calcular_preco_medio(data):
    '''
    Recebe a lista de anúncios e retorna o preço médio das acomodações.
    '''

    total_price = 0
    for anuncio in data:
        total_price += float(anuncio['price'])
    return total_price / len(data)


def anuncio_mais_caro(data):
    '''
    Recebe a lista de anúncios e retorna um dicionário com todas as informações da acomodação com o preço mais alto.
    '''

    mais_caro = max(data, key=lambda x: float(x['price']))

    return mais_caro


def bairro_maior_menor_media_preco(data):
    '''
    Recebe a lista de anúncios e retorna os bairros que possuem a maior e menor media de preços e seus respectivos valores.
    '''

    bairros = {}
    for anuncio in data:
        if anuncio['neighbourhood'] in bairros:
            bairros[anuncio['neighbourhood']].append(float(anuncio['price']))
        else:
            bairros[anuncio['neighbourhood']] = [float(anuncio['price'])]

    media_bairros = {bairro: sum(prices) / len(prices) for bairro, prices in bairros.items()}
    maior_preco = max(media_bairros, key=media_bairros.get)
    menor_preco = min(media_bairros, key=media_bairros.get)

    return maior_preco, media_bairros[maior_preco], menor_preco, media_bairros[menor_preco]


def gerar_relatorio_airbnb(airbnb):
    '''
    Utiliza as funções acima para gerar um relatório com as seguintes inforamções sobre os anúncios do Airbnb:
    Número total de anúncios.
    Bairro com o maior número de anúncios.
    Preço médio das acomodações.
    Anúncio com o preço mais alto.
    Bairro com a maior média de preço.
    Bairro com a menor média de preço.
    O formato do relatório deve ser:

        RELATÓRIO AIRBNB
    Total de anúncios: [total_anuncios]
    Bairro com mais anúncios: [bairro_com_mais_anuncios]
    Preço médio: [preco_medio]
    Anúncio mais caro: [anuncio_mais_caro_info]
    Bairro mais caro e bairro mais barato: [bairro_maior_menor_media]
    '''

    data = ler_arquivo(airbnb)
    total_anuncios = contar_anuncios(data)
    bairro_com_mais_anuncios = bairro_mais_anuncios(data)
    preco_medio = calcular_preco_medio(data)
    anuncio_mais_caro_info = anuncio_mais_caro(data)
    bairro_maior_menor_media = bairro_maior_menor_media_preco(data)

    relatorio = f'''
    RELATÓRIO AIRBNB
Total de anúncios: {total_anuncios}
Bairro com mais anúncios: {bairro_com_mais_anuncios}
Preço médio: {preco_medio}
Anúncio mais caro: {anuncio_mais_caro_info}
Bairro mais caro e bairro mais barato: {bairro_maior_menor_media}
'''
    return relatorio

print(gerar_relatorio_airbnb('airbnb.csv'))