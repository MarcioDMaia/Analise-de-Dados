import requests
from bs4 import BeautifulSoup


class InfoGoogle:
    def __init__(self, keyword, start_date, max_date):

    # Define a palavra-chave
        self.keyword = keyword

    # Define a data atual e a data de início do período de tempo desejado
        self.start_date = start_date

    # Define o valor de cd_max
        self.cd_max = max_date

        self.url = ""

    def URLReplace(self):
    # Monta a URL da pesquisa com o filtro de data
        self.url = f"https://www.google.com/search?q={self.keyword}&tbs=cdr%3A1%2Ccd_min%3A{self.start_date}%2Ccd_max%3A{self.cd_max}&ei=xxxxx&start=0&sa=N&ved=xxxxx&safe=active&ssui=on"
        self.url = self.url.replace("xxxxx", "")  # Substitua 'xxxxx' pelos valores corretos do parâmetro ei e ved


    def RequestHTTP(self):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(self.url, headers=headers)

        soup = BeautifulSoup(response.content, "html.parser")

        result_stats = soup.find("div", {"id": "result-stats"})

        if result_stats:
            result_stats_text = result_stats.text
    # Extrai apenas o número de resultados a partir da string

            num_results = int("".join(filter(str.isdigit, result_stats_text)))
            return num_results
        
        else:
            return None


    # Test preview

if __name__ == "__main__":
    info = InfoGoogle("Ciência da Computação", "01/01/2021", "01/01/2022")
    info.URLReplace()
    print(info.RequestHTTP())
