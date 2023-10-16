import requests

class ApiRequest:
    """Classe principal"""

    def __init__(self):
        """Método construtor da classe"""
        self.dados = []

    
    def request_api(self, categoria):
        """Método para fazer requisição da api"""

        # chave da API e url para requisição
        API_KEY = 'sua chave de api da newsapi'
        site =f'https://newsapi.org/v2/top-headlines?country=br&category={categoria}&apiKey={API_KEY}'

        # retornar o response e converter e json
        response = requests.get(site)
        self.dados = response.json()
        self.dados = self.dados['articles']

        # chamada da método da classe
        return self.criar_lista_api()


    def criar_lista_api(self):
        """Método para construir uma lista a partir do json"""

        lista_noticias = []

        for dado in self.dados:
            lista_noticias.append(dado['url'])

        return lista_noticias
    