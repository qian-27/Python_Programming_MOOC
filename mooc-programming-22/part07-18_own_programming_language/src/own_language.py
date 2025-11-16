# Write your solution here
def run(program):
   dict = {}
   print_list = []
   i = 0

   while i < len(program):
      for string in program:
         if "PRINT" in string:
            new_string = string.split()
            the_var = new_string[1]
            if the_var in dict:
               print_list.append(dict[the_var])
            else:
               print_list.append(0)
            i += 1
            # print(f"it's PRINT, {dict[the_var]}")
         elif "MOV" in string:
            new_string = string.split()
            try:
               dict[new_string[1]] = int(new_string[2])
            except:
               dict[new_string[1]] = int(dict[new_string[2]])
            i += 1
            # print(f"{new_string[1]} = {new_string[2]}")
         elif "ADD" in string:
            new_string = string.split()
            result1 = int(dict[new_string[1]])
            try:
               new_result = result1 + int(new_string[2])
            except:
               result2 = int(dict[new_string[2]])
               new_result = result1 + result2
            dict[new_string[1]] = new_result
            i += 1
            # print(f"it's ADD,{dict[new_string[1]]} = {new_result}")
         elif "SUB" in string:
            new_string = string.split()
            result1 = int(dict[new_string[1]])
            try:
               new_result = result1 - int(new_string[2])
            except:
               result2 = int(dict[new_string[2]])
               new_result = result1 - result2
            dict[new_string[1]] = new_result
            i += 1
            # print(f"it's SUB,{old_result}, {new_result}")
         elif "MUL" in string:
            new_string = string.split()
            result1 = int(dict[new_string[1]])
            try:
               new_result = result1 * int(new_string[2])
            except:
               result2 = int(dict[new_string[2]])
               new_result = result1 * result2
            dict[new_string[1]] = new_result
            i += 1
            # print("it's MUL")
         elif "END" in string:
            # exit()
            i += 1
            if len(print_list) > 0:
               return print_list
            else:
               text = "[]"
               return text

   return print_list  

# You can test your function by calling it within the following block
if __name__ == "__main__":
   # program1 = []
   # program1.append("MOV A 1")
   # program1.append("MOV B 2")
   # program1.append("SUB B 1")
   # program1.append("PRINT A")
   # program1.append("PRINT B")
   # program1.append("ADD A B")
   # program1.append("PRINT A")
   # program1.append("END")
   # result = run(program1)
   # print(result)
   
   program1 = ['PRINT A', 'END'] 
   result = run(program1)
   print(result)