import csv

def ler_dados_csv (nome_arquivo, ano):
    
        '''
        Lê os dados do arquivo csv e retorna uma lista de dicionários, onde cada dicionário representa uma partida ocorrida no ano indicado.

        Os dados são separados em:
        'rodada' (int) : o número da rodada, 'data' (datetime): a data da partida, 'mandante' (str) : o time mandante, 'visitante' (str) : o time visitante, 'mandante_gols' (int) : o número de gols do time mandante, 'visitante_gols' (int) : o número de gols do time visitante  e 'vencedor' (str) :o time vencedor da partida (em caso de empate o valor é '-').
        '''

        with open(nome_arquivo, 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            dados = [linha for linha in leitor if linha['data'].endswith(str(ano))]
        return dados


def contar_partidas (dados):
     
     '''
     Recebe a lista de partidas no arquivo CSV e retorna o número total de partidas.
     '''
     
     return len(dados)



def time_com_mais_vitorias (dados):
    
    '''
    Recebe a lista de partidas no arquivo CSV e retorna o nome do time com o maior número de vitórias.

    o time vencedor de cada partida é representado pela string 'vencedor' no dicionário de cada partida.
    '''

    vitorias = {}
    for partida in dados:
        if partida['vencedor'] != '-':
            if partida['vencedor'] in vitorias:
                vitorias[partida['vencedor']] += 1
            else:
                vitorias[partida['vencedor']] = 1
    return max(vitorias, key=vitorias.get)



def calcular_media_gols (dados):
    '''
    Recebe a lista de partidas e retorna a média de gols por partida.

    A quantidade de gols marcados em cada partida é representada pelas chaves 'mandante_gols' e 'visitante_gols' no dicionário de cada partida.

    A média de gols por partida é calculada pela soma de todos os gols marcados dividida pelo total de partidas.
    '''

    total_gols = 0
    for partida in dados:
        total_gols += int(partida['mandante_gols']) + int(partida['visitante_gols'])
    return total_gols / len(dados)



def partida_com_maior_numero_de_gols (dados):

    '''
    Recebe a lista de partidas e retorna a partida com o maior número de gols.

    A partida com o maior número de gols é aquela em que a soma dos gols marcados pelo time mandante e visitante é a maior.

    Retorna um dicionário com as informações da partida com o maior número de gols.
    '''

    return max(dados, key=lambda x: int(x['mandante_gols']) + int(x['visitante_gols']))



def gerar_relatorio_brasileirao (nome_arquivo, ano):

    '''
    Utiliza as funções anteriores para gerar um relatório com as estatisticas do Campeonato Brasileiro de futebol de determinado ano.
    
    Gera  um relatório com as estatisticas do Campeonato Brasileiro de futebol de determinado ano.

    Parametros:
        nome_arquivo (str) : nome do arquivo csv de onde os dados serão lidos
        ano (int) : ano do campeonato a ser analisado

    Retorna:
        relatorio (str) : string com as estatisticas do campeonato  

    Formato do relatorio:
        Relatório do Campeonato Brasileiro de [ano]:
        --------------------
        Total de partidas: [total_partidas]
        Time com mais vitórias: [jogador_mais_vitorias]
        Média de gols por partida: [media_gols]
        Partida com maior número de gols:
             Rodada: [rodada_maior_gols]
             Time mandante: [mandante_maior_gols] - Gols: [gols_mandante_maior_gols]
             Time visitante: [visitante_maior_gols] - Gols: [gols_visitante_maior_gols]
             Vencedor: [vencedor_maior_gols]
    '''

    dados = ler_dados_csv(nome_arquivo, ano)
    total_partidas = contar_partidas(dados)
    time_mais_vitorias = time_com_mais_vitorias(dados)
    media_gols = calcular_media_gols(dados)
    maior_gols = max(dados, key=lambda x: int(x['mandante_gols']) + int(x['visitante_gols']))
    rodada_maior_gols = maior_gols['rodada']
    mandante_maior_gols = maior_gols['mandante']
    gols_mandante_maior_gols = maior_gols['mandante_gols']
    visitante_maior_gols = maior_gols['visitante']
    gols_visitante_maior_gols = maior_gols['visitante_gols']
    vencedor_maior_gols = maior_gols['vencedor']

    relatorio = f'Relatório do Campeonato Brasileiro de {ano}:\n'
    relatorio += '--------------------\n'
    relatorio += f'Total de partidas: {total_partidas}\n'
    relatorio += f'Time com mais vitórias: {time_mais_vitorias}\n'
    relatorio += f'Média de gols por partida: {media_gols}\n'
    relatorio += f'Partida com maior número de gols:\n'
    relatorio += f'Rodada: {rodada_maior_gols}\n'
    relatorio += f'Time mandante: {mandante_maior_gols} - Gols: {gols_mandante_maior_gols}\n'
    relatorio += f'Time visitante: {visitante_maior_gols} - Gols: {gols_visitante_maior_gols}\n'
    relatorio += f'Vencedor: {vencedor_maior_gols}\n'

    return relatorio

print(gerar_relatorio_brasileirao('brasileirao.csv', 2019))