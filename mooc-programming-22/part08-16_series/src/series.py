# Write your solution here:
class Series:
   def __init__(self, name: str, season: int, genre: list):
      self.name = name
      self.season = season
      self.genre = genre
      self.rate_list = []
      self.title = name

   def rate(self, rating: int):
      if rating >= 0 and rating <= 5:
         self.rate_list.append(rating)

   def average_points(self):
      return sum(self.rate_list) / len(self.rate_list)
   
   def __str__(self):
      text = f"{self.name} ({self.season} seasons)\ngenres: {', '.join(self.genre)}\n"
      if len(self.rate_list) == 0:
         text += "no ratings"
      else:
         text += f"{len(self.rate_list)} ratings, average {self.average_points():.1f} points"
      return text




def minimum_grade(grade: float, series: list):
   my_list = []
   for item in series:
   # item = s1/s2/s3
      if item.average_points() > grade:
         my_list.append(item)
   return my_list

def includes_genre(genre: str, series: list):
   my_list = []
   for item in series: 
   # item = s1/s2/s3
      if genre in item.genre:
         my_list.append(item)
   return my_list


# You can test your function by calling it within the following block
if __name__ == "__main__":
   s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
   s1.rate(5)

   s2 = Series("South Park", 24, ["Animation", "Comedy"])
   s2.rate(3)

   s3 = Series("Friends", 10, ["Romance", "Comedy"])
   s3.rate(2)

   series_list = [s1, s2, s3]

   print("a minimum grade of 4.5:")
   for series in minimum_grade(4.5, series_list):
       print(series.title)

   print("genre Comedy:")
   for series in includes_genre("Comedy", series_list):
      print(series.title)


# Answers!!!
# class Series:
#     def __init__(self, title: str, seasons: int, genres: list):
#         self.title = title
#         self.seasons = seasons
#         self.genres = genres
#         self.ratings = [0, 0, 0, 0, 0, 0]
#         self.number_of_ratings = 0
 
#     def grade(self):
#         if self.number_of_ratings == 0:
#             return 0
#         else:
#             grade_sum = 0
#             for i in range(0, 6):
#                 grade_sum += self.ratings[i] * i
#             return grade_sum / self.number_of_ratings
 
 
#     def __str__(self):
#         genres = ", ".join(self.genres)
 
#         if self.number_of_ratings == 0:
#             ratings = "no ratings"
#         else:
#             grade_sum = 0
#             for i in range(0, 6):
#                 grade_sum += self.ratings[i] * i
#             ka = grade_sum / self.number_of_ratings
#             ratings = f"{self.number_of_ratings} ratings, average {ka:.1f} points"
 
#         return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{ratings}"
 
#     def rate(self, grade: int):
#         self.number_of_ratings += 1
#         self.ratings[grade] += 1
 
# def minimum_grade(grade: float, seriest: list):
#     result = []
#     for series in seriest:
#         if series.grade() >= grade:
#             result.append(series)
 
#     return result
 
# def includes_genre(genre: str, seriest: list):
#     result = []
#     for series in seriest:
#         if genre in series.genres:
#             result.append(series)
 
#     return result