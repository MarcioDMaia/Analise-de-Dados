import urllib.request
import io
import numpy as np
import PyPDF2

class ExtractionTableWord:
    def __init__(self, url, word, total_pages, save_name=""):

        # Número total de páginas
        self.total_pages = total_pages
        
        # URL do arquivo PDF
        self.url = url

        # Como a tabela será salva
        self.save_name = save_name
        
        # Palavra desejada
        self.word = word

        # Carrega o PDF online
        self.response = urllib.request.urlopen(self.url)
        self.pdf_contents = self.response.read()

        
        # Cria um objeto de leitura do PDF
        self.pdf_reader = PyPDF2.PdfReader(io.BytesIO(self.pdf_contents))
        
        # Intância uma lista que posteriormente salva a nota dos alunos que foram aprovados no curso que se deseja analisar
        self.grades = []

        self.Search()

        self.mean = np.mean(self.grades)
        
    def Search(self):
        # Procura linhas que possuam o curso desejado
        for page in range(self.total_pages):

            # Procura na página da interação
            pag = self.pdf_reader.pages[page]
            # Estrai apenas o texto da tabela
            table_text = pag.extract_text().split('\n')
            
            for line in table_text:            
                # Caso tenha, o aluno é introduzido numa lista
                   if (self.word.lower() in line.lower()):
            
                    self.grades.append(float(line.split()[-3].replace(",", ".")))


if __name__== "__main__":
    exemple = ExtractionTableWord("https://prograd.ufc.br/wp-content/uploads/2019/11/edital-028-2019-transferencia-de-outras-ies-e-admissao-de-graduados-2020-1-aprovados.pdf", "File1", "Ciência da computação", 14)
