from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify("<h1>Hello!</h1>")

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Validamos que el body sea un diccionario con 'label' y 'done'
    if not isinstance(request_body, dict) or 'label' not in request_body or 'done' not in request_body:
        return jsonify({ "error": "El cuerpo debe contener 'label' y 'done'" }), 400

    # Agregamos el nuevo todo
    todos.append(request_body)

    # Devolvemos la lista actualizada
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición inválida"}), 404

    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

