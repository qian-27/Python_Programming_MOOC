# Write your solution here
def store_personal_data(person: tuple):
   name = person[0]
   age = person[1]
   height = person[2]

   with open("people.csv", "a") as file:
      file.write(f"{name};{age};{height}\n")

# You can test your function by calling it within the following block
if __name__ == "__main__":
   person = ("Paul Paulson", 37, 175.5)
   store_personal_data(person)

# def store_personal_data(person: tuple):
#     with open("people.csv", "a") as file:
#         row = person[0] + ";"
#         row += str(person[1]) + ";"
#         row += str(person[2])
 
#         file.write(row + "\n")