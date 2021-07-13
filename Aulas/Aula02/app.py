from flask import Flask, request
import json 

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id': id,'person': 'Pedro', 'work': 'developer'})

@app.route('/soma/<int:value1>/<int:value2>')
def soma(value1, value2):
    return jsonify({'value1': value1, 'value2': value2, 'total': value1 + value2})

@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        soma = sum(dados['values'])
        return jsonify({'soma': soma}) 
    elif request.method == 'GET':
        soma = 10 + 10
        return jsonify({'soma': soma}) 


if __name__ == "__main__":
    app.run(debug=True)
