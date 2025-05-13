from flask import Flask, jsonify, request

app = Flask (__name__)
livros = [
    {
        'id': 1,
        'título': 'Crepúsculo',
        'autor': 'Stephenie Meyer'
    },
    {
        'id': 2,
        'título': 'Entrevista com o Vampiro',
        'autor': 'Anne Rice'
    },
    {
        'id': 3,
        'título': 'Drácula',
        'autor': 'Bram Stoker'
    }
]

#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar todos(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:  #pq livro?
        if livro.get ('id')== id:
            return jsonify (livro)

#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def obter_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify (livros)
#excluir   
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livro_excluido = request.get_json
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livro[indice]
    return jsonify (livros)

app.run(port=5000,host='localhost',debug=True)