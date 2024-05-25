"""
API - é um lugar para disponibilizar recursos e/ou funcionalidades

1. Objetivo - Criar uma API que disponibliliza consulta , criação , edição e exclusão de livros.

2. URL base - localhost

3. EndPoints -
- localhost/livros (GET)
- localhost/livros/id (GET)
- localhost/livros/id (PUT)
- localhost/livros/id (DELETE)

4. Quais recursos - Livros
"""
__version__ = "0.1.0"
__author__ = "Gabriel Victor"
__license__ = "Unlincese"

from flask import Flask , jsonify , request

app = Flask(__name__)

livros =  [
  {
    'id': 1,
    'titulo': 'Código Limpo',
    'autor': 'Robert Cecil Martin'
  } ,
  {
    'id': 2,
    'titulo': ' O Programador Pragmático',
    'autor': 'Andy Hunt e Dave Thomas'
  },
  {
    'id': 3,
    'titulo':'Trabalho Eficaz com Código Legado',
    'autor': 'Michael C. Feathers'
  }
]

# Consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
  return jsonify(livros)

# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
  for livro in livros:
    if livro.get('id') == id:
      return jsonify(livro)

# editar
@app.route('/livros/<int:id>' , methods=['PUT'])
def editar_livro_por_id(id):
  livro_alterado = request.get_json()
  for indice , livro in enumerate(livros):
    if livro.get('id') == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

# criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)
  return jsonify(livros)

# excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
  for indice, livro in enumerate(livros):
    if livro.get('id') == id:
      del livros[indice]
  return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
