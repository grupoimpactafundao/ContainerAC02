from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    lista = ['Nome: Mateus Casanova Montesso. Ra: 2200492',
             'Nome: Tarcisio Eugenio de Albuquerque Ferreira. Ra: 2200174',
             'Nome: Vinicius Farias Albanit. Ra: 2200420',
             'Nome: Joao Vitor Lima Telesi. Ra: 2201224']
    return "<br>".join(lista)




if __name__ == '__main__':
    app.run()