# Write your solution here
def spruce(num):
    print("a spruce!")

    space = num - 1
    space2 = num - 1
    s = 1

    while num > 0:
        print(" " * space + "*" * s)
        space -= 1
        s += 2
        num -= 1

    print(" " * space2 + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)