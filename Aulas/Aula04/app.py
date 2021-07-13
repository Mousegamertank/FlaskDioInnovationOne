from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from habilidades import ListaHabilidades, Habilidades
import json 

app = Flask(__name__)
api = Api(app)

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

class Developer(Resource):
    def get(self, id):
        if request.method == 'GET':
            try:
                response = developers[id]
            except IndexError:
                response = {'status': 'error', 'message': 'developer {} dont exist'.format(id)}
            except Exception:
                mensagem = 'Error, look for the admin'
                response = {'status': 'error', 'message': mensagem}
            return response

    def put(self, id):
        dados = json.loads(request.data)
        developers[id] = dados
        return dados    

    def delete(self, id):
        developers.pop(id)
        return {'status': 'successuful', 'mensagem': '{} deleted '.format(id)}


class ListDevelopers(Resource):
    def get(self):
        return developers

    def post(self):
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return developers[posicao]

api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(ListaHabilidades, '/habilidades')
api.add_resource(Habilidades, '/habilidades/<int:id>')


if __name__ == "__main__":
    app.run(debug=True)