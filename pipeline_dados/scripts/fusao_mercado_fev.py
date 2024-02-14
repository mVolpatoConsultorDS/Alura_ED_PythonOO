import json
import csv

def leitura_json(path_json):
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
        return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spam_reader = csv.DictReader(file, delimiter = ',')
        for row in spam_reader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    else:
        print('Tipo de Arquivo nao Suportado')
        return
    return dados

def get_columns(dados):
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

def size_data(dados):
    return len (dados)

def join(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

def transformando_dados_tabela(dados, nome_columnas):
    dados_combinados_tabela = [nome_columnas]
    for row in dados:
        linha = []
        for coluna in nome_columnas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = '/Users/miltonvolpato/Google Drive/Alura/Alura_ED_PythonOO/pipeline_dados/data_raw/dados_empresaA.json'
path_csv = 'pipeline_dados/data_raw/dados_empresaB.csv'
path_dados_combinados = 'pipeline_dados/data_prosseded/dados_combinados.csv'

# Iniciando a Leitura
dados_json = leitura_dados(path_json, 'json')
nome_columnas_json = get_columns(dados_json)
print(nome_columnas_json)
print(size_data(dados_json))
dados_csv = leitura_dados(path_csv, 'csv')
nome_columnas_csv = get_columns(dados_csv)
print(nome_columnas_csv)

##Transformacao dos Dados
key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque':'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda':'Data da Venda'}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_columnas_csv = get_columns(dados_csv)
print(f'Nomes das Colonas do csv: {nome_columnas_csv}')
print(size_data(dados_csv))

dados_fusao = join(dados_json, dados_csv)
nome_columnas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print(nome_columnas_fusao)
print(tamanho_dados_fusao)

# Verificar nomes de colunas
if get_columns(dados_fusao) == get_columns(dados_csv):
    print("Os nomes das colunas estão corretos.")
    print(nome_columnas_fusao)
    print(nome_columnas_csv)
else: 
    print(nome_columnas_fusao)
    print(nome_columnas_csv)
    print("Os nomes das colunas nao baten.")

# Verificar total de linhas
if size_data(dados_fusao) == size_data(dados_json) + size_data(dados_csv):
    print("O total de linhas está correto.")


#salvar
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_columnas_csv)
# Verificar nomes de colunas
if dados_fusao_tabela[0] == get_columns(dados_csv):
    print("Os nomes das colunas estão corretos.")
    print(dados_fusao_tabela[0])
    print(nome_columnas_csv)
else: 
    print(dados_fusao_tabela[0])
    print(nome_columnas_csv)
    print("Os nomes das colunas nao baten.")

salvando_dados(dados_fusao_tabela, path_dados_combinados)