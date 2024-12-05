import os
import csv
import pdfplumber
import re

# Caminho da pasta com os PDFs
pasta_pdfs = "C:\\Users\\Matheus\\Documents\\Programação\\Python\\trabalho"

# Nome do arquivo CSV de saída
arquivo_csv = "nome_idade_pessoas.csv"

# Lista para armazenar os dados extraídos temporariamente
dados_extraidos = []

# Função para extrair o nome da pessoa
def extrair_nome(texto):
    # Supondo que o nome esteja precedido de "Nome:" no texto
    match = re.search(r"Nome:\s*([A-Za-z\s]+)", texto)
    return match.group(1).strip() if match else "Nome não encontrado"  # Valor padrão se o nome não for encontrado

# Função para extrair a idade da pessoa
def extrair_idade(texto):
    # Supondo que a idade esteja precedida de "Idade:" no texto
    match = re.search(r"Idade:\s*(\d+)", texto)
    return int(match.group(1)) if match else None  # Valor padrão se a idade não for encontrada

# Verifica se a pasta existe
if os.path.isdir(pasta_pdfs):
    for arquivo in os.listdir(pasta_pdfs):
        if arquivo.endswith(".pdf"):  # Verifica se o arquivo é um PDF
            caminho_pdf = os.path.join(pasta_pdfs, arquivo)
            print(f"Processando: {caminho_pdf}")

            # Extração de texto com pdfplumber
            with pdfplumber.open(caminho_pdf) as pdf:
                for numero_pagina, pagina in enumerate(pdf.pages, start=1):
                    texto = pagina.extract_text()
                    if texto:  # Verifica se a página tem texto
                        nome = extrair_nome(texto)  # Extrai o nome da pessoa
                        idade = extrair_idade(texto)  # Extrai a idade da pessoa
                        if idade is not None:  # Apenas armazena se a idade for encontrada
                            dados_extraidos.append((nome, idade))

    # Ordena os dados pelo nome (alfabeticamente) e pela idade (crescente) caso os nomes sejam iguais
    dados_extraidos.sort(key=lambda x: (x[0], x[1]))  # Ordena pelo nome, depois pela idade

    # Escreve os dados ordenados no arquivo CSV
    with open(arquivo_csv, "w", newline="", encoding="utf-8") as csvfile:
        escritor_csv = csv.writer(csvfile)
        escritor_csv.writerow(["Nome", "Idade"])  # Cabeçalhos do CSV
        for dado in dados_extraidos:
            escritor_csv.writerow(dado)  # Escreve nome e idade

    print(f"Processamento concluído! Dados salvos em {arquivo_csv}")
else:
    print("A pasta especificada não foi encontrada ou não é válida.")
