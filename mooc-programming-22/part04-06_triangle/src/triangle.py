# Copy here code of line function from previous exercise
def line(num, text):
    print(num * text)

def triangle(size):
    x = 1
    while size > 0:
        line(x, "#")
        x += 1
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
