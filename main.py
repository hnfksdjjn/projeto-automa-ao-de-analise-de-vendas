from dados import carregar_dados, tratar_dados, gerar_analise
from relatorio import criar_relatorio
from email_sender import enviar_email
import os

# Caminhos
CAMINHO_BASE = "arquivos/vendas.xlsx"
CAMINHO_RELATORIO = "arquivos/relatorio.pdf"

def main():
    # 1. Carregar dados
    df = carregar_dados(CAMINHO_BASE)
    if df is None:
        return

    # 2. Tratar dados
    df = tratar_dados(df)

    # 3. Gerar análises
    resumo, totais = gerar_analise(df)

    # 4. Criar relatório
    criar_relatorio(resumo, totais, CAMINHO_RELATORIO)

    # 5. Enviar relatório por e-mail
    enviar_email(CAMINHO_RELATORIO)

if __name__ == "__main__":
    main()
