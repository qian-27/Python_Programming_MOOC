# Write your solution here
def line(num, text):

    if len(text) >= 1:
        char = text[0]
        print(char * num)
    elif text =="":
        print("*" * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    # line(5, "x")
    line(5, "")