# Ingredient Checker

# Step1:- Define the recipe ingredients
recipe_ingredients = {"flour","sugar","butter","eggs","milk"}

# step2:- Get user input for available ingredients

user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

# step3: Compare Ingredients

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

#  step4 :- Display Results
print("\n--- Ingredients Check Result---\n")
if missing_ingredients:
    print(f"you are missing the following ingredients: {', '.join(extra_ingredients)} ")
else:
    print("you have all the ingredients needed.")

if extra_ingredients:
    print(f"You have extra ingredients : {', '.join(extra_ingredients)}")
else:
    print("you have all the ingredients needed")
