import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

class Deputados:
    def __init__(self):
        plt.rcParams["figure.figsize"] = (2, 2)
        self.lista = []

    def requisicao(self):
        url = "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
        headers = {'Content-type': 'application/json'}

        data = ''

        request = requests.get(url=url, data=data, headers=headers)

        # Retorno completo do json
        dados = json.loads(request.content)
        dados = dados['dados']

        for dado in dados:
            self.lista.append([dado['nome'], dado['siglaPartido'], dado['siglaUf']])

        deputados = pd.DataFrame(self.lista)
        deputados.columns = ['nome', 'partido', 'uf']
        print(deputados)

        deputados_partido = deputados.groupby('partido')['nome'].count()
        deputados_partido = deputados_partido.reset_index()
        grafico_dep_partido = plt.barh(width=deputados_partido.nome, y=deputados_partido.partido)
        plt.savefig('dados/static/dados/images/deputadosxpartido.png', dpi=100)
        print(deputados_partido)

        # Limpeza do cachê do matplotlib
        plt.clf()

        deputados_uf = deputados.groupby('uf')['nome'].count()
        deputados_uf = deputados_uf.reset_index()
        grafico_dep_uf = plt.barh(width=deputados_uf.nome, y=deputados_uf.uf)
        plt.savefig("dados/static/dados/images/deputadosxuf.png")
        print(deputados_uf)


if __name__ == '__main__':
    camara = Deputados()
    camara.requisicao()