# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
   result = "".join([w for w in string if any(l in forbidden for l in w) == False])
   return result


# Answers!!!
# def filter_forbidden(string: str, forbidden: str):
#    return "".join([character for character in string if character not in forbidden])



# You can test your function by calling it within the following block
if __name__ == "__main__":
   sentence = "Once! upon, a time: there was a python!??!?!"
   filtered = filter_forbidden(sentence, "!?:,.")
   print(filtered)