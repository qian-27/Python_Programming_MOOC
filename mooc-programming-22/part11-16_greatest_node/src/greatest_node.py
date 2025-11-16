# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    max_node = root.value

    if root.left_child is not None and greatest_node(root.left_child) > max_node:
        max_node = greatest_node(root.left_child)
    if root.right_child is not None and greatest_node(root.right_child) > max_node:
        max_node = greatest_node(root.right_child)
    
    return max_node



# You can test your function by calling it within the following block
if __name__ == "__main__":
    tree = Node(3)

    tree.left_child = Node(5)
    tree.left_child.left_child = Node(7)
    tree.left_child.left_child = Node(10)

    tree.right_child = Node(3)
    tree.right_child.right_child = Node(13)
    tree.right_child.right_child = Node(6)
    tree.right_child.right_child = Node(11)

    print(greatest_node(tree))



# Answers!!!
# class Node:
#     """ Class is modeling single node in binary tree """
#     def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
#         self.value = value
#         self.left_child = left_child
#         self.right_child = right_child
 
# def greatest_node(root: Node):
#     value = root.value
 
#     if root.left_child:
#         left_value = greatest_node(root.left_child)
#     else:
#         left_value = value
 
#     if root.right_child:
#         right_value = greatest_node(root.right_child)
#     else:
#         right_value = value
 
#     return max(value, left_value, right_value)