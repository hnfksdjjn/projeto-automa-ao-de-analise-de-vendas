import pandas as pd

def carregar_dados(caminho_arquivo):
    """Carrega dados do Excel e retorna um DataFrame."""
    try:
        df = pd.read_excel(caminho_arquivo)
        print("Dados carregados com sucesso.")
        return df
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def tratar_dados(df):
    """Aplica limpeza e tratamento nos dados."""
    # Exemplo de limpeza
    df.dropna(inplace=True)  # Remove linhas com valores nulos
    df.columns = [col.strip() for col in df.columns]  # Remove espaços nos nomes das colunas
    print("Dados tratados com sucesso.")
    return df

def gerar_analise(df):
    """
    Gera um resumo estatístico com count, mean e std.
    """
    # Gera o resumo com todas as estatísticas e seleciona apenas as desejadas
    resumo = df.describe().loc[['count', 'mean', 'std']]
    
    
    # Calcula totais adicionais se necessário
    totais = df.count()  # Total de valores por coluna
    
    print("Análise gerada com sucesso.")
    return resumo, totais
