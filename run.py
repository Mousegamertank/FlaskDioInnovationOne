from flask import Flask, jsonify, request
import json 

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)


#---------------------------------------------
# PRIMEIRA AULA DE FLASK PELA DIO
# @app.route("/<numero>", methods=['GET', 'POST'])
# def heloo(numero):
#     return {'messsage': 'Hello World {}'.format(numero)}

#---------------------------------------------
# SEGUNDA AULA DE FLASK PELA DIO
# @app.route('/<int:id>')
# def pessoa(id):
#     return jsonify({'id': id,'person': 'Pedro', 'work': 'developer'})

# @app.route('/soma/<int:value1>/<int:value2>')
# def soma(value1, value2):
#     return jsonify({'value1': value1, 'value2': value2, 'total': value1 + value2})

# @app.route('/soma', methods=['POST', 'PUT', 'GET'])
# def soma():
#     if request.method == 'POST':
#         dados = json.loads(request.data)
#         soma = sum(dados['values'])
#         return jsonify({'soma': soma}) 
#     elif request.method == 'GET':
#         soma = 10 + 10
#         return jsonify({'soma': soma}) 

#----------------------------------------------
# TERCEIRA AULA DE FLASK PELA DIO

# developers = [
#     {'id' : 0,
#      'name': 'Pedro', 
#      'habilities': ['Python', 'Flask']
#     },
#     {'id': 1,
#      'name': 'Rafa',
#      'habilities': ['Python', 'Django']
#     }
# ]

# @app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# def developer(id):
#     if request.method == 'GET':
#         try:
#             response = developer[id]
#         except IndexError:
#             response = {'status': 'error', 'message': 'developer {} dont exist'.format(id)}
#         except Exception:
#             mensagem = 'Error, look for the admin'
#             reponse = {'status': 'error', 'message': messagem}
#         return jsonify(response)

#     elif request.method == 'PUT':
#         dados = json.loads(request.data)
#         developers[id] = dados
#         return jsonify(dados)
    
#     elif request.method == 'DELETE':
#         developers.pop(id)
#         return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})

# @app.route('/dev', methods=['GET', 'POST'])
# def addeveloper():
#     if request.method == 'GET':
#         return jsonify(developers)
#     elif request.method == 'POST':
#         dados = json.loads(request.data)
#         posicao = len(developers)
#         dados['id'] = posicao
#         developers.append(dados)
#         return jsonify(developers[posicao])
    
#----------------------------------------------
# QUARTA AULA DE FLASK PELA DIO

