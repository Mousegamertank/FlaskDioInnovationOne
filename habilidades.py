from flask_restful import Resource
import json

habilidades = [
    {'tech': 'Python', 'id': 0},
    {'tech': 'Java', 'id': 1}, 
    {'tech': 'Flask', 'id': 2}, 
    {'tech': 'PHP', 'id': 3}
    ]

class ListaHabilidades(Resource):
    def get(self):
        return habilidades

    def post(self):
        data = json.loads(request.data)
        habilidades.append(data)
        return habilidades

class Habilidades(Resource):
    def get(id):
        try:
            return habilidades[id]
        except:
            return {'message': 'Dont exist the id'}

    def put(id):
        data = json.loads(request.data)
        habilidade[id] = data
        return habilidade[id]

    def delete(id):
        habilidades.pop(id)
        try:
            mensagem = 'success'
        except:
            mensagem = 'failed'

        return {'message': mensagem}
        