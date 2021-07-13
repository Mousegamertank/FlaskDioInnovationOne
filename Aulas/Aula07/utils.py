from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(name='Pedro', idade='19')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # try: 
    #     pessoa = Pessoas.query.filter_by(name='Pedro H S').first()
    # except:
    #     return None
    # # for p in pessoa:
    # #     print(p)
        
    # print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(name='Pedro H S').first()
    pessoa.name = 'Pedro H S'
    pessoa.idade = 18
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(id=2).first()
    pessoa.delete()

def inseri_usuarios(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuario = Usuarios.query.all()
    print( usuario )
 
if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
    # inseri_usuarios('john', 1234)
    consulta_todos_usuarios()