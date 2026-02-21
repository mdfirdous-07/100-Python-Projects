# Recipe Viewer App

FILE_NAME = "recipes.txt"

# Load Recipes
def load_recipes():
    recipes = {}

    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()

        if not content:
            return recipes

        blocks = content.split("\n\n")

        for block in blocks:
            lines = block.split("\n")

            if len(lines) >= 3:
                name = lines[0].strip()
                ingredients = lines[1].replace("Ingredients:", "").strip()
                instructions = lines[2].replace("Instructions:", "").strip()

                recipes[name] = {
                    "ingredients": ingredients,
                    "instructions": instructions
                }

    except FileNotFoundError:
        pass

    return recipes



# Display Menu
def show_menu():
    print("\n" + "-" * 30)
    print("      RECIPE VIEWER")
    print("1. View Recipe")
    print("2. List All Recipes")
    print("3. Add New Recipe")
    print("4. Exit")


# View Recipe 
def view_recipe(recipes):
    search_name = input("Enter recipe name: ").strip().lower()

    for name in recipes:
        if name.lower() == search_name:
            print(f"Recipe: {name}")
            print("-" * 30)
            print("Ingredients:", recipes[name]["ingredients"])
            print("Instructions:", recipes[name]["instructions"])
            return

    print("Recipe not found.")



# List Recipes
def list_recipes(recipes):
    if not recipes:
        print("No recipes available.")
        return

    print("\nAvailable Recipes:")
    for index, name in enumerate(recipes.keys(), start=1):
        print(f"{index}. {name}")



# Add New Recipe

def add_recipe(recipes):
    name = input("Enter new recipe name: ").strip()

    # Check duplicate (case-insensitive)
    for existing in recipes:
        if existing.lower() == name.lower():
            print("Recipe already exists.")
            return

    ingredients = input("Enter ingredients: ").strip()
    instructions = input("Enter instructions: ").strip()

    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions
    }

    # Append file
    with open(FILE_NAME, "a+") as file:
        file.seek(0)
        content = file.read()

        if content.strip():
            file.write("\n")

        file.write(f"{name}\n")
        file.write(f"Ingredients: {ingredients}\n")
        file.write(f"Instructions: {instructions}\n")

    print("Recipe added successfully!")


# Main Program

def main():
    recipes = load_recipes()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_recipe(recipes)

        elif choice == "2":
            list_recipes(recipes)

        elif choice == "3":
            add_recipe(recipes)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()  
