from recipe_finder import extract_ingredients_from_input, find_recipes, print_recipe
from recipe_parser import import_recipes

def main():
    data_path: str = "./data/recipes.json"
    ingredients_raw: str = input("Enter a list of ingredients, separated by commas: ")

    ingredients_parsed: list[str] = extract_ingredients_from_input(ingredients_raw)
    recipes_list: list[dict] = import_recipes(data_path)
    recipes_found: list[dict] = find_recipes(ingredients_parsed, recipes_list)

    if len(recipes_found) > 0:
        print()
        for r in recipes_found:
            print_recipe(r)
    else:
        print("No recipes found.")

    

if __name__ == "__main__":
    main()