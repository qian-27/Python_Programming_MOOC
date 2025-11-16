# Copy here code of line function from previous exercise and use it in your solution
def line(size, character):
    print(size * character)

def shape(num1, char1, num2, char2):
        x = 1
        while num1 > 0:
            line(x, char1)
            x += 1
            num1 -= 1
        
        x = x - 1

        while num2 > 0:

            line(x, char2)
            num2 -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")