# Write your solution here
def find_movies(database: list, search_term: str):
   new_list = []

   for dictionary in database:
      if search_term.capitalize() in dictionary["name"]:
         new_list.append(dictionary)

   
   return new_list
   

# def find_movies(database: list, search_term: str):
#     found_ones = []
#     for movie in database:
#         # The function lower() converts a string to lowercase
#         # when this is done for both strings search is case insensitive
#         if search_term.lower() in movie["name"].lower():
#             found_ones.append(movie)
 
#     return found_ones



# You can test your function by calling it within the following block
if __name__ == "__main__":
   database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
   {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
   {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

   my_movies = find_movies(database, "Python")
   print(my_movies)