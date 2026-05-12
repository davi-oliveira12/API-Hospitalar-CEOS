from flask import Flask, make_response, jsonify, request
from bd2 import Pacientes
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#GET - listar todos os pacientes
@app.route('/pacientes', methods=['GET']) 
def get_pacientes():
    return make_response(
        jsonify(
            mensagem = 'Lista com todos os pacientes',
            pacientes =Pacientes
            )
        )

#POST - criar novo paciente
@app.route('/pacientes', methods=['POST'])
def adicionar_jogadores():
    paciente = request.json
    Pacientes.append(paciente)
    return jsonify(mensagem='Paciente adicionado com sucesso.'), 201


#DELETE - deletar um paciente
@app.route('/pacientes/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    for i in Pacientes:
        if i['id'] == id:
            Pacientes.remove(i)
            return jsonify(mensagem =f'Paciente {id} deletado com sucesso'), 200
        return jsonify(mensagem=f'Paciente {id} não consta no hospital.'), 404
    
app.run()
print('hello world')