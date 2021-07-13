from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        try:
            response = {
                'name': pessoa.name,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa not found'
            }
        return response

    def put(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        dados = request.json
        try:
            if 'name' in dados:
                pessoa.name = dados['name']

            if 'idade' in dados:
                pessoa.idade = dados['idade']
                pessoa.save()
                response = {
                    'id': pessoa.id,
                    'name': pessoa.name,
                    'idade': pessoa.idade
                } 
        except:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa not found'
            }
        return response

    def delete(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        try:
            pessoa.delete()
            return {'status': 200, 'message': 'deleted successuful'}
        except:
            return {'status': 400, 'message': 'could not find the user to delete'}

class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'name': i.name, 'idade': i.idade} for i in pessoas]
        return response
    
    def post(self):
        data = request.json
        pessoa = Pessoas(name=data['name'], idade=data['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'name': pessoa.name,
            'idade': pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'name': i.name, 'pessoa': i.pessoa.name} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(name=dados['pessoa']).first()
        atividade = Atividades(name=dados['name'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa' : atividade.pessoa.name,
            'name' : atividade.name
        }
        return response 

api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(Pessoa, '/pessoa/<string:name>')
api.add_resource(ListaPessoas, '/pessoas/')

if __name__ == '__main__':
    app.run(debug=True  )