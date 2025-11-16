# Write your solution here
from shutil import move


def add_movie(database: list, name: str, director: str, year: int, runtime: int):
   database.append({"name": name, "director": director, "year": year, "runtime": runtime})

# You can test your function by calling it within the following block
if __name__ == "__main__":
   database = []
   add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
   add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
   print(database)

# def add_movie(database: list, name: str, director: str, year: int, runtime: int):
#     # Python accepts splitting rows from punctuation
#     # The addition becomes more readable when parts are divided into separate rows
#     movie = {"name": name,
#                "director": director,
#                "year": year,
#                "runtime": runtime}
 
#     database.append(movie)