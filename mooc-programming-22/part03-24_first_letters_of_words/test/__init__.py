# Write your solution here
sentence = input("Please type in a sentence: ")

word = sentence.split()

i = 0

while i < len(word):
    print(word[i][0])
    i += 1