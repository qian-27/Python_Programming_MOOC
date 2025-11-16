# Write your solution here
word1 = input("Please type in the 1st word:").lower()
word2 = input("Please type in the 2nd word:").lower()

if word1 != word2:
    if word1 > word2:
        print(f"{word1} comes alphabetically last.")
    else:
        print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")
    