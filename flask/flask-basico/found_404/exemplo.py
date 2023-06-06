# importar o pacote 
import flask

# seria tipo criar um objeto do tipo flask
app =  flask.Flask(__name__)

@app.route("/")
def main():
	return "Ola´, mundo!"

@app.route("/pagina")
def pagina():
	return "PAGINA 1"

@app.errorhandler(404)
def pagina_nao_encontrado(e):
    return "Sempre que a pagina nao existir vai cair aqui, precisa passa esse e como parametro"

#debug so usa em caso de producao
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
