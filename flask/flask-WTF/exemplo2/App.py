from flask import Flask, render_template, url_for, session, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField)

# TextField,

from wtforms.validators import DataRequired


app = Flask(__name__)

# Importante ter para podemo criar formulario
app.config['SECRET_KEY'] = 'chave_secreta'


class Formulario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    casado = BooleanField('Voce e casado')
    sexo = RadioField('Sexo:', choices= [('h', 'homem'), ('m', 'mulher')])
    cor = SelectField('Cor favorito:', choices = [('v', 'vermellho'), ('a', 'azul')])
    comentario = TextAreaField()
    enviar = SubmitField('Enviar')

@app.route('/informacao')
def informacao():
    return render_template('informacao.html')


@app.route('/dados', methods=['GET', 'POST'])
def dados():

    formulario = Formulario()

    #verifica se foi prenchido e enviado
    if formulario.validate_on_submit():
        # Pegando o valor
        #session não é uma lista qualquer, foi importado do flask
        session['nome'] = formulario.nome.data
        session['casado'] = formulario.casado.data
        session['sexo'] = formulario.sexo.data
        session['cor'] = formulario.cor.data
        session['comentario'] = formulario.comentario.data
        return redirect(url_for('informacao'))

    return render_template('dados.html', formulario=formulario)

if __name__ == '__main__':
    app.run(debug=True)

