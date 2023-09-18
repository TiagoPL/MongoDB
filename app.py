from flask import Flask, jsonify
from pymongo import MongoClient

client = MongoClient(host='172.21.1.3', port=27017)
db = client['project_521']

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Home page'

@app.route('/usuarios')
def get_usuarios():
    return jsonify([{"_id": str(usuario['_id']), "name": usuario.get("name")} for usuario in db.usuario.find()])

@app.route('/usuarios/<name>')
def get_usuario(name):
    return jsonify([{"_id": str(usuario["_id"]), "name": usuario.get("name")} for usuario in db.usuario.find({"name": name})])

@app.route('/adicionar/<nome>')
def add_user(nome):
    db.usuario.insert_one({"name": nome})
    return f'Usuario {nome} adicionado no banco de dados!'

@app.route('/remover/<nome>')
def del_user(nome):
    db.usuario.delete_one({"name": nome})
    return f'Usuario {nome} removido do banco de dados'

@app.route('/replace/<nome>/<novo_nome>')
def replace_user(nome, novo_nome):
    busca = {"name": nome}
    new_values = {"$set": {'name': novo_nome}}

    db.usuario.update_one(busca, new_values)
    return jsonify(f'User {nome} has been updated to {novo_nome} in the DataBase')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
