from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

developers = [
    {'id' : 0,
     'name': 'Pedro', 
     'habilities': ['Python', 'Flask']
    },
    {'id': 1,
     'name': 'Rafa',
     'habilities': ['Python', 'Django']
    }
]

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':
        try:
            response = developer[id]
        except IndexError:
            response = {'status': 'error', 'message': 'developer {} dont exist'.format(id)}
        except Exception:
            mensagem = 'Error, look for the admin'
            reponse = {'status': 'error', 'message': messagem}
        return jsonify(response)

     
    
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})

@app.route('/dev', methods=['GET', 'POST'])
def addeveloper():
    if request.method == 'GET':
        return jsonify(developers)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return jsonify(developers[posicao])

if __name__ == "__main__":
    app.run(debug=True)
    