from flask import Flask, request, jsonify

app = Flask(__name__)

# simple in-memory storage
pantry = []

@app.route('/pantry', methods=['GET'])
def get_pantry():
    return jsonify({"pantry": pantry})

@app.route('/pantry', methods=['POST'])
def add_ingredient():
    data = request.get_json()
    ingredient = data.get("ingredient")

    if not ingredient:
        return jsonify({"error": "No ingredient provided"}), 400

    pantry.append(ingredient.lower())
    return jsonify({"message": "Ingredient added", "pantry": pantry})

if __name__ == '__main__':
    app.run(port=5001)