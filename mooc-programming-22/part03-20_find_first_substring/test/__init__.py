# Write your solution here
word = input("Please type in a word: ")
character = input("Please type in a character: ")
len_word = len(word)

start = word.find(character)
end = start + 3

if start != -1 and len_word >= end:
    print(word[start:end])