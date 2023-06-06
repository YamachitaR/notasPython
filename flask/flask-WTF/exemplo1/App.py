from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'


class Formulario(FlaskForm):
    nome = StringField('Nome')
    enviar = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    nome = ''
    enviado = False
    formulario = Formulario()

    #verifica se foi prenchido e enviado
    if formulario.validate_on_submit():
        # Pegando o valor
        nome = formulario.nome.data
        enviado = True
        formulario.nome.data = ''

    return render_template('index.html', formulario=formulario, enviado=enviado, nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
