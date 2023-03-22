import urllib.request
import io
import PyPDF2

class ExtractionTablePage:

    def __init__(self, url, pag, state, course):

        # Intância as variaveis que armazenarão as notas dos aprovados e os da lista de espera
        self.approved = []
        self.waiting_list = []
        

        # Intância uma linha de corte para o curso que se deseja analisar
        self.course = f"{course.strip().upper()} - {state.strip().upper()}"
        self.state = state

        # Carrega o PDF online
        self.response = urllib.request.urlopen(url)
        self.pdf_contents = self.response.read()

        # Cria um objeto de leitura do PDF
        self.pdf_reader = PyPDF2.PdfReader(io.BytesIO(self.pdf_contents))

        # Extraí a tabela de uma página específica e deixa apenas as informações do curso desejado
        self.page = self.pdf_reader.pages[pag]
        self.table_text = self.page.extract_text().split('\n')
        self.separate_table_by_desired_course()

        # Cria uma lista que tem contida apenas as notas e se foi ou não aprovado
        self.grades = []
        self.separate_data()
        

    def separate_data(self):

        # Separa os aprovados dos que estão na lista de espera
        for i in self.table_text:
            if i.split()[-1] == "vaga":
                self.grades.append([i.split()[-3], 1])

            else:
                self.grades.append(i.split()[-1])

        # percorre as notas e separa em aprovados e reporvados
        for i in self.grades:
            
            try:
                if (i[-8:] == "APROVADO"):
                    self.approved.append(float(i[:6]))

            except IndexError:
                pass

            try:
                if (i[0][-15:] == "Desclassificado"):
                    self.waiting_list.append(float(i[0][:6].strip()))

            except IndexError:
                continue

            
    
    def separate_table_by_desired_course(self, first=0):

    
        if (first == 0):
        # Percorre a tabela e procura o curso
            for i, j in enumerate(self.table_text):

            # Abrange dois casos: Primeiro, a tabela possui mais curso depois do escolhido; segundo quando ela é a ultima
                if (self.state.strip().upper() in j) and (i > self.table_text.index(self.course)):
                    self.table_text = self.table_text[self.table_text.index(self.course):i]
                    break

                else:
                    self.table_text = self.table_text[self.table_text.index(self.course):]
                    
                
        else:

            for i, j in enumerate(self.table_text):
                if (self.state.strip().upper() in j):
                    self.table_text =  self.table_text[:i]
                    break

                else:
                    self.table_text =  self.table_text





# Exemplo que será futuramente apagado

if __name__ == "__main__":
    df = ExtractionTablePage("https://prograd.ufc.br/wp-content/uploads/2022/11/edital-22-2022-transferencia-de-outras-ies-aprovados-e-desclassificados-por-vaga-2023-1.pdf", 1, "fortaleza", "ciência da computação")
