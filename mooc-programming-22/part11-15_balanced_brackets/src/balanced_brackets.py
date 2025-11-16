# WRITE YOUR SOLUTION HERE:
def balanced_brackets(my_string: str):
    new_string = "".join([word for word in my_string if word in "()[]"])
    # print(new_string)

    if len(new_string) == 0:
        return True
    if not (new_string[0] == '[' and new_string[-1] == ']') and not (new_string[0] == '(' and new_string[-1] == ')'):
        return False

    # remove first and last character
    return balanced_brackets(new_string[1:-1])



# You can test your function by calling it within the following block
if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)



# Answers!!!
# def balanced_brackets(mj: str):
#     # string is empty, so it is ok
#     if len(mj) == 0:
#         return True
 
#     # if first character is not any bracket, let's eat it away
#     if not mj[0] in "()[]":
#         return balanced_brackets(mj[1:])
 
#     # if last is not any bracket, let's eat it away
#     if not mj[-1] in "()[]":
#         return balanced_brackets(mj[:-1])
    
#     # now is known that first and last characters are brackets
#     # check if they are a pair
#     if mj[0]=="(" and mj[-1]==")":
#         return balanced_brackets(mj[1:-1])
#     if mj[0]=="[" and mj[-1]=="]":
#         return balanced_brackets(mj[1:-1])
 
#     # were not, so this string is not ok
#     return False