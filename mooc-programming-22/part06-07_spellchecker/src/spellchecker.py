# write your solution here
text = input("Write text: ")

text_lowercase = text.lower()
words = text_lowercase.split()

with open("wordlist.txt") as new_file:
   same_words = []
   for line in new_file:
      line = line.replace("\n", "")
      if line in words:
         same_words.append(line)
   # print(same_words)
   for word in words:
      if word not in same_words:
         newword = f"*{word}*"
         text = text.replace(word, newword)

print(text)


# def wordlist():
#     words = []
 
#     with open("wordlist.txt") as file:
#         for row in file:
#             words.append(row.strip())
 
#     return words
 
# words = wordlist()
# sentence = input("Write text: ")
 
# for word in sentence.split(' '):
#     if word.lower() in words:
#         print(word + " ", end="")
#     else:
#         print("*" + word + "* ", end="")
 
# print()



