# Recipe Finder and Meal Planner Microservice System

## Description

This project is a microservice-based recipe finder and meal planner built using Python and Flask. The goal of the system is to allow a user to input ingredients they already have and receive meal recommendations based on those ingredients.

The system is made up of three separate services: a Pantry Service, a Recipe Service, and a Planner Service. These services communicate with each other using HTTP requests and exchange data in JSON format. The Recipe Service also integrates with the Spoonacular API to retrieve real recipe data.

---

## Installation

Make sure Python 3 is installed on your system.

Install required packages using:

```bash
pip install flask requests
```

---

## Running the System

Each service must be run in a separate terminal window.

Run the Pantry Service:

```bash
python pantry_service.py
```

Run the Recipe Service:

```bash
python recipe_service.py
```

Run the Planner Service:

```bash
python planner_service.py
```

---

## Using the CLI

The project includes a simple command-line interface for interacting with the system.

Run the CLI:

```bash
python cli.py
```

From the menu, you can:

* Add ingredients to the pantry
* View current pantry contents
* Generate meal recommendations

---

## Alternative API Usage (Optional)

The system is primarily intended to be used through the CLI, but the API endpoints can also be tested directly using tools such as curl.

Add an ingredient using curl:

```bash
curl -X POST http://127.0.0.1:5001/pantry -H "Content-Type: application/json" -d "{\"ingredient\":\"chicken\"}"
```

View pantry:
http://127.0.0.1:5001/pantry

Get recommendations:
http://127.0.0.1:5000/plan

---

## System Design Notes

The system is designed using a microservice architecture where each service has a specific responsibility. The Pantry Service stores user ingredients, the Recipe Service retrieves and formats recipe data, and the Planner Service combines the data to generate recommendations.

All communication between services is done through HTTP requests, and all data is exchanged using JSON. The Planner Service calculates a match score based on how many ingredients from a recipe are available in the pantry.

---

## Known Issues

* The Spoonacular API sometimes returns inconsistent or overly detailed ingredient descriptions
* The pantry data is stored in memory and will reset when the service is restarted
* The free API key has request limits

---

## API Key Note

This project requires a Spoonacular API key to run the Recipe Service.

Insert your API key in `recipe_service.py`:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---
