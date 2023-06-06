from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'


class Formulario(FlaskForm):
    nome = StringField('Nome')
    enviar = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    formulario = Formulario()

    #verifica se foi prenchido e enviado
    if formulario.validate_on_submit():
        # Pegando o valor
        nome = formulario.nome.data
        flash("Obrigado {}! ".format(nome))
        return redirect(url_for('index'))

    return render_template('index.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)
