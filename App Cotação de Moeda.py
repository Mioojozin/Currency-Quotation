import requests
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file('tela.kv')

class Aplicativo(App):
    def build(self):
        return GUI
    box = BoxLayout(orientation = 'vertical')

    def on_start(self):
        self.root.ids['moeda1'].text = f"Dólar R${self.pegar_coracao('USD')}"
        self.root.ids['moeda2'].text = f"Euro R${self.pegar_coracao('EUR')}"
        self.root.ids['moeda3'].text = f"BitCoin R${self.pegar_coracao('BTC')}"
        self.root.ids['moeda4'].text = f"Etherium R${self.pegar_coracao('ETH')}"


    def pegar_coracao(self, moeda):
        link = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f'{moeda}BRL']['bid']
        return cotacao


Aplicativo().run()