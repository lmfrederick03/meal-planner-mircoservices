from flask import Flask, jsonify
import requests

app = Flask(__name__)

# helper function to calculate match score
def calculate_match_score(recipe_ingredients, pantry):
    matches = [i for i in recipe_ingredients if i in pantry]
    return len(matches) / len(recipe_ingredients)

@app.route('/plan', methods=['GET'])
def plan_meals():
    try:
        # get pantry data
        pantry_response = requests.get("http://127.0.0.1:5001/pantry")
        pantry_data = pantry_response.json()
        pantry = pantry_data.get("pantry", [])

        if not pantry:
            return jsonify({"error": "Pantry is empty"}), 400

        # get recipes
        ingredient_string = ",".join(pantry)
        recipe_response = requests.get(
            f"http://127.0.0.1:5002/recipes?ingredients={ingredient_string}"
        )
        recipe_data = recipe_response.json()
        recipes = recipe_data.get("recipes", [])

        # calculate match scores
        recommendations = []

        for recipe in recipes:
            score = calculate_match_score(recipe["ingredients"], pantry)

            recommendations.append({
                "name": recipe["name"],
                "matchScore": round(score, 2)
            })

        return jsonify({"recommendations": recommendations})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)