from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html') 
# repare que home.html esta dentro do diretorio templates.
# O proprio flask vai procura por diretorio denominado templates, por isso que tem ser o nome templates

if __name__ == '__main__':
    app.run(debug=True)

