# Write your solution here
def chessboard(length):
    i = 0

    while i < length:
        if i % 2 == 0:
            text = "10"*length
        else:
            text = "01"*length
        
        print(text[0:length])
        i += 1


# Testing the function
if __name__ == "__main__":
    chessboard(5)