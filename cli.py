import requests

BASE_URL = "http://127.0.0.1"

def add_ingredient():
    ingredient = input("Enter an ingredient: ").strip()

    if not ingredient:
        print("No ingredient entered.")
        return

    response = requests.post(
        f"{BASE_URL}:5001/pantry",
        json={"ingredient": ingredient}
    )

    print(response.json())


def view_pantry():
    response = requests.get(f"{BASE_URL}:5001/pantry")
    print(response.json())


def get_recommendations():
    response = requests.get(f"{BASE_URL}:5000/plan")
    print(response.json())


def menu():
    while True:
        print("\nMeal Planner CLI")
        print("1. Add ingredient")
        print("2. View pantry")
        print("3. Get meal recommendations")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_ingredient()
        elif choice == "2":
            view_pantry()
        elif choice == "3":
            get_recommendations()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()