# Write your solution here
def range_of_list(list_name):
    maxi_num = max(list_name)
    mini_num = min(list_name)
    result = maxi_num - mini_num
    return result
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)