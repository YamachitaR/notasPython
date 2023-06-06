from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página inicial'

@app.route('/about')
def about():
    return 'Sobre nós'

@app.route('/user/<username>')
def profile(username):
    return f'Perfil do usuário: {username}'

with app.test_request_context():
    print(url_for('home'))               # Output: /
    print(url_for('about'))              # Output: /about
    print(url_for('profile', username='john'))  # Output: /user/john

