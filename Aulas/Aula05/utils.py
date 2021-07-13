from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(name='HPedro H S', idade='19')
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()

    try: 
        pessoa = Pessoas.query.filter_by(name='Pedro H S').first()
    except:
        return None
    # for p in pessoa:
    #     print(p)
        
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(name='Pedro H S').first()
    pessoa.name = 'Pedro H S'
    pessoa.idade = 18
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(name='Pedro H S').first()
    pessoa.delete()
 
if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    consulta_pessoas()
