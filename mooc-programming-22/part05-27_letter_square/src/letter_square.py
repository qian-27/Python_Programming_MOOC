# Write your solution here


# layer = int(input("Give a number between 2 and 26: "))
# table_size = layer + layer - 1
# ts = table_size
# center = (ts // 2)
# counter=0
# for row in range(ts):
#         for col in range(ts):
#                 if row<=center and ts-counter>col:
#                     outcome=65+center-min(row,col)
#                 elif row <=center and col>=ts-counter :
#                     outcome=65+col-center   
#                 elif row>center and ts-counter>col:
#                     outcome=65+center-min(row,col)  
#                 elif row >center and col<counter :   
#                     outcome=65+row-center
#                 elif row >center and col>=counter :   
#                     outcome=65+row-center+(col-counter)                   
                
#                 print(chr(outcome), end="")
#         counter=counter+1        
               
#         print()



n = int(input("Layers: "))
 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1
while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1