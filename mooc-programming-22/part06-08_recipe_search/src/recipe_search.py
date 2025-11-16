# # Write your solution here

# write a empty line at the end of the file
f = open("recipes1.txt", "a")
f.write("\n")
f.close()

f = open("recipes2.txt", "a")
f.write("\n")
f.close()


def read_file(filename: str):
    with open(filename) as new_file:
        recipes = {"r_name":"recipe"}
        recipe = []
        for line in new_file:
            if line == "\n":
                recipes[recipe[0]] = recipe[1:]
                recipe.clear()
                continue
            recipe.append(line.strip())
        return recipes
 
def search_by_name(filename:str, word: str):
    recipes = read_file(filename)
    found_recipes = []
    #recipes[r_name] = [time, ingredient, ingredient, etc]
    for key, recipe in recipes.items():
        if word.lower() in key.lower():
            new_line = "\n"
            # found_recipes += key+ "\n" 
            found_recipes.append(key)
    return found_recipes


# def search_by_time(filename: str, prep_time: int):
#    # Pancakes, preparation time 15 min


# def search_by_ingredient(filename: str, ingredient: str):
#    # Pancakes, preparation time 15 min
 

# You can test your function by calling it within the following block
# if __name__ == "__main__":
#     found = search_by_name("recipes1.txt", "cake")
#     print(found)
#     for recipe in found:
#         print(recipe)

