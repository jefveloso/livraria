from flask import flask, jsonify, request
app = flask (neme)
livros = [
    {
        'id: 1,'
        'título': MESSI
        'autor': Ariel Senociain
    },
    {
        'ide':2,
        'titulo' Cabeça Fria Coração Quente
        'autor': Abel Fereira
    },
    {
        'id'3,
        'titulo': O telefone Preto 
        'autor': Joe Hill
    },
]

@ app.raute('/livros', methads =['get']) 
def obter_livros():
    return jsinify

@ app. raute ('/livros /<int:id>', methads = ['get'])
def obter_livros_id(id):
    for livros in livros:
        if livros.get('id') == id:
            return jsonify(livros)
    
@ app.raute ('/livros/<int:id>', methods=['put'])
def eeditar_livros_por_id(id):
    livros_alterados = request.get_json()
    for indice,livros in enumerate(livros):
        if livros.get('id') == id:
            livros[indice].update(livros_alterados)
            return jsonify(livros[indice])    

@app.raute('/livros/', mathads = ['post'])
def incluir_novo_livros():
    novo_livros= request.get_json()
    livros.append(novo_livros)
    return jsonify(livros)

@app.raute('/livros/<int:id>', methads = ['delete'])
def  excluir_livros(id):
    if livros.get('id') == id:
        def livros [indicie]
        return jsonify(livros)

@apprum(port=5000,hast='localpost',delbug=True)