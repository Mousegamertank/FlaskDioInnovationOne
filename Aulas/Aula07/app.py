from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIO = {
#     'rafael': '123',
#     'Pedro': '321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     else:
#         return USUARIO.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    else:
        return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
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

    @auth.login_required
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

    @auth.login_required
    def delete(self, name):
        pessoa = Pessoas.query.filter_by(name=name).first()
        try:
            pessoa.delete()
            return {'status': 200, 'message': 'deleted successuful'}
        except:
            return {'status': 400, 'message': 'could not find the user to delete'}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'name': i.name, 'idade': i.idade} for i in pessoas]
        return response
    
    @auth.login_required
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
    @auth.login_required
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'name': i.name, 'pessoa': i.pessoa.name} for i in atividades]
        return response

    @auth.login_required
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

    #EXERCICIOS PARA PRATICA 
    '''
    INCLUIR PARA MODELAGEM ATIVIDADES na qual retorna todas as atividades pelo nome da pessoa responsavel
    MODELAGEM ATIVIDADES - campo Status (Pendente, Concluido)
    Atraves do ID da atividade permitir consultar e alterar o Status da atividade
    Tratativa de excessões em todos os metodos na qual ira retornar uma mensagem caso o registro não exista
    '''