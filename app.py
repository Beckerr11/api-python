from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/usuario")
def usuario():
    return jsonify({
        "nome": "Douglas",
        "curso": "Ciência da Computação"
    })

app.run(debug=True)