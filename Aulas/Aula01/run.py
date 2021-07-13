from flask import Flask, request

app = Flask(__name__)

@app.route("/<numero>", methods=['GET', 'POST'])
def heloo(numero):
    return {'messsage': 'Hello World {}'.format(numero)}


if __name__ == "__main__":
    app.run(debug=True)

