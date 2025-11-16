# Write your solution here

name_Editor = input("Editor: ").lower()

while True:
   if name_Editor == "visual studio code":
      print("an excellent choice!")
      break
   elif name_Editor == "word" or name_Editor == "notepad":
      print("awful")
      name_Editor = input("Editor: ").lower()
   else:
      print("not good")
      name_Editor = input("Editor: ").lower()