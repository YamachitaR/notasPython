# importar o pacote 
import flask

# seria tipo criar um objeto do tipo flask
app =  flask.Flask(__name__)

@app.route("/")

def main():
	return "Ola´, mundo!"

#debug so usa em caso de producao
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
