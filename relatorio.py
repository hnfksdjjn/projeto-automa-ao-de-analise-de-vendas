from fpdf import FPDF

class PDFRelatorio(FPDF):
    """Classe personalizada para criar relatórios mais elegantes com tabelas."""

    def header(self):
        """Cabeçalho do relatório."""
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Relatório de Análise de Dados', border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        """Rodapé do relatório."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Página {self.page_no()}', align='C')

    def adicionar_tabela(self, titulo, dataframe):
        """Adiciona uma tabela com título e conteúdo do DataFrame, com as métricas e valores em duas colunas."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, titulo, ln=True)
        self.ln(5)

        # Ajuste da largura das colunas
        col_width = 60  # Largura das colunas

        # Adicionar as métricas de cada coluna
        self.set_font('Arial', '', 10)

        for col in dataframe.columns:
            # Nome da coluna
            self.cell(col_width, 10, col, border=1, align='C')
            self.ln()
            
            # Adicionar os dados para cada métrica (count, mean, std)
            for metric in ['count', 'mean', 'std']:
                self.cell(col_width, 10, metric, border=1, align='C')
                self.cell(col_width, 10, str(dataframe.at[metric, col]), border=1, align='C')
                self.ln()

    def adicionar_lista(self, titulo, lista_dados):
        """Adiciona uma lista de dados formatada no relatório."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, titulo, ln=True)
        self.ln(5)
        self.set_font('Arial', '', 10)
        for item in lista_dados:
            self.cell(0, 10, f"- {item}", ln=True)
        self.ln(5)

    def adicionar_total(self, total):
        """Adiciona o total de vendas no relatório, formatado com 3 casas decimais."""
        self.set_font('Arial', 'B', 12)
        # Formatar o total de vendas com 3 casas decimais
        total_formatado = f"{total:.1f}"
        self.cell(0, 10, f"Total de Vendas: {total_formatado} milhoes", ln=True)
        self.ln(5)


def criar_relatorio(resumo, totais, caminho_relatorio):
    """Gera um relatório em PDF formatado."""
    pdf = PDFRelatorio()
    pdf.add_page()

    # Adicionar resumo estatístico
    pdf.adicionar_tabela("Resumo Estatístico (count, mean, std)", resumo)

    # Adicionar nomes das colunas
    colunas_lista = [f"{col}" for col in totais.index]
    pdf.adicionar_lista("Nomes das Colunas", colunas_lista)

    # Calcular o total de vendas (somando os valores da coluna 'vendas')
    if 'VENDAS' in resumo.columns:
        total_vendas = resumo['VENDAS'].sum()
    else:
        total_vendas = 0

    # Adicionar o total de vendas no relatório
    pdf.adicionar_total(total_vendas)

    # Salvar o relatório
    pdf.output(caminho_relatorio)
    print(f"Relatório gerado: {caminho_relatorio}")
