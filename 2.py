ingredients = ["1 tbsp cilantro", "2 avocados", "1 lime", "1 tsp salt", "1/2 onion"]

def add_ingredient(ingredient):
    ingredients.append(ingredient)


def pop_ingredient():
    ingredients.pop()


def pop_ingredient_at(index):
    ingredients.pop(index)


def count_ingredients():
    return len(ingredients)


def pretty_recipe():
    print(f"The number of ingredients needed is: {count_ingredients()}")
    tabbed = "\n \t * ".join(ingredients)
    print(tabbed)



def search_for_ingredient(ingredient):
    for i in range(len(ingredients)):
        if ingredients[i] == ingredient:
            print(f"{ingredient} is in the list, the counter is :{i}")
            break
        else:
            if i < len(ingredients) - 1:
                continue
            else:
                print("Item not in list but has been added now")
                ingredients.append(ingredient)
                break

add_ingredient("tomatoes")
pop_ingredient()
pop_ingredient_at(0)
print(count_ingredients())
pretty_recipe()
search_for_ingredient("hello")
print(ingredients)