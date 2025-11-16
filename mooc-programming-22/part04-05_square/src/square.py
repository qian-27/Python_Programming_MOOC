# Copy here code of line function from previous exercise
def line(num, text):
    print(num * text)

def square(size, character):
    x = size
    while size > 0:
        line(x, character)
        size -= 1
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")