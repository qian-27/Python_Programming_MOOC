# Write your solution here
def first_word(sentence):
    word_Array = sentence.split()
    first = word_Array[0]
    return first

def second_word(sentence):
    word_Array = sentence.split()
    second = word_Array[1]
    return second

def last_word(sentence):
    word_Array = sentence.split()
    last = word_Array[-1]
    return last

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))