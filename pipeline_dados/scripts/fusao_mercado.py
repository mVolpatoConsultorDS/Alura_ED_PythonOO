import os

from processamento_dados import Dados

def main():
    os.system('clear')
    path_json = '/Users/miltonvolpato/Google Drive/Alura/Alura_ED_PythonOO/pipeline_dados/data_raw/dados_empresaA.json'
    path_csv = '/Users/miltonvolpato/Google Drive/Alura/Alura_ED_PythonOO/pipeline_dados/data_raw/dados_empresaB.csv'
    path_dados_combinados = '/Users/miltonvolpato/Google Drive/Alura/Alura_ED_PythonOO/pipeline_dados/data_prosseded/dados_combinados.csv'

    #extract
    dados_empresaA = Dados(path_json, 'json')
    print(dados_empresaA.nome_colunas)
    print(dados_empresaA.qtd_linhas)
    dados_empresaB = Dados(path_csv, 'csv')
    print(dados_empresaB.nome_colunas)
    print(dados_empresaB.qtd_linhas)
    
    #transform
    key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque':'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda':'Data da Venda'}
    dados_empresaB.rename_columns(key_mapping)
    print(dados_empresaB.nome_colunas)

    dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
    print(dados_fusao.nome_colunas)
    print(dados_fusao.qtd_linhas)

    #load
    dados_fusao.salvando_dados(path_dados_combinados)
    print(path_dados_combinados)

if __name__ == '__main__':
    main()