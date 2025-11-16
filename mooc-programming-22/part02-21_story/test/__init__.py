# Write your solution here
words = []
length = 0

while True:
    word = input("Please type in a word: ")
    words.append(word)
    length += 1
    if word == "end":
        break
    if length >= 2 and words[length - 1] == words[length - 2]:
        break
# length = len(words)
print(" ".join(words[0 : length - 1]))