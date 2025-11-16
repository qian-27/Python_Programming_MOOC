# Write your solution here
def squared(text, num):
    i = 0
    index = 0

    while True:
        if i >= num:
            break
        
        lengthOfText = num**2

        if len(text) < lengthOfText:
            text *= lengthOfText
        
        # print(i)
        # print(index)

        print(text[index:index+num])
        i += 1
        index += num

# Testing the function
if __name__ == "__main__":
    squared("aybabtu", 5)