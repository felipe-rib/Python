from fpdf import FPDF

# Criação de uma classe derivada de FPDF para personalizar o cabeçalho e rodapé
class PDF(FPDF):
    def header(self):
        # Fonte do cabeçalho
        self.set_font('Times', 'B',10)
        # Título do cabeçalho
        self.cell(0, 10, 'Gerência de Suporte Remoto - GSUP', 0, 1, 'R')
        self.ln(10)

    def footer(self):
        # Posiciona 1,5 cm do final da página
        self.set_y(-15)
        # Fonte do rodapé
        self.set_font('Arial', 'I', 8)
        # Número da página
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Criação do objeto PDF
pdf = PDF()

# Definindo uma margem para o documento
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.set_top_margin(12)
pdf.set_left_margin(10)


# Adicionando uma página
pdf.add_page()

# Configurando a fonte do título
pdf.set_font('Arial', 'B', 14)

# Adicionando um título
pdf.cell(0, 10, '1. Descrição', 0, 1, 'L')
pdf.ln(5) #distância da quebra de linha

# Configurando a fonte para o corpo do texto
pdf.set_font('Arial', '', 12)

# Adicionando um texto
texto = """O Relatório Informacional de Downloads e Estatísticas (RIDE) é um documento que apresenta dados e métricas relacionadas à atividade de download e uso das Plataformas PostgreSYS e TDP."""
pdf.multi_cell(0, 7, texto) #altura, largura e escrita
pdf.ln(4)

texto = """O RIDE tem como objetivo acompanhar o desempenho e uso das Plataformas:"""
pdf.multi_cell(0, 7, texto)

# Adicionando um título
pdf.set_font('Arial', 'B', 14) # Configurando a fonte do título
pdf.cell(0, 10, '2. Downloads das Plataformas Full', 0, 1, 'L')
pdf.ln(5) #distância da quebra de linha


##############################################################################################################

# Adicionando uma página
pdf.add_page()


# Adicionando um título
pdf.set_font('Arial', 'B', 14) # Configurando a fonte do título
pdf.cell(0, 10, '2.1 Versões das Plataformas', 0, 1, 'L')
pdf.ln(5) #distância da quebra de linha

# Adicionando uma imagem
pdf.ln(10)
pdf.image('grafico.png', x=20, y=None, w=100)  # Note que a imagem é ajustada para respeitar a margem esquerda



# Salvando o arquivo PDF
pdf.output('relatorio_fpdf.pdf')
