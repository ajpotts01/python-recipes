def print_recipe(recipe: dict) -> None:
    print(f"Recipe: {recipe['name']}")
    print(f"Ingredients: {','.join(recipe['ingredients'])}")
    print(f"Instructions: {recipe['instructions']}")
    print()

def extract_ingredients_from_input(ingredients: str) -> list[str]:
    result: list[str] = [i.strip() for i in ingredients.split(",")]

    return result

def find_recipes(ingredients: list[str], recipes: list[dict]) -> list[dict]:
    result: list[dict] = []

    # Don't check if each specified ingredient is in a recipe
    # Do it the other way around to avoid issue of returning partial matches
    result = [r for r in recipes if all(i in ingredients for i in r["ingredients"])]

    return result

