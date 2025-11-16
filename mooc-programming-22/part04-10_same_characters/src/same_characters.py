# Write your solution heref
def same_chars(text, a, b):
    if a >= len(text) or b >= len(text):
        return False
    elif text[a] == text[b]:
        return True
    elif text[a] != text[b]:
        return False



        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))