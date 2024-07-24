from flask import Flask, url_for, render_template
from routes.home import home_route
from routes.cliente import cliente_route
# Faz a importação dos recursos, "flask" é o módulo e "Flask" a classe.

# inicializacao
app = Flask(__name__)

# rotas
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False}
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return "<h1>Gestão de Pessoas</h1>"

# execucao
app.run(debug=True)