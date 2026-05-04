from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_SPOONACULAR_API_KEY"  # Replace with your actual Spoonacular API key

@app.route('/recipes', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients')

    if not ingredients:
        return jsonify({"error": "No ingredients provided"}), 400

    try:
        url = "https://api.spoonacular.com/recipes/findByIngredients"

        params = {
            "ingredients": ingredients,
            "number": 5,
            "apiKey": API_KEY
        }

        response = requests.get(url, params=params)
        data = response.json()

        results = []

        for recipe in data:
            results.append({
                "name": recipe["title"],
                "ingredients": ingredients.split(","),
                "missingIngredients": [i["name"].split(",")[0] for i in recipe.get("missedIngredients", [])]
            })

        return jsonify({"recipes": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5002)