class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:
def order_by_length(route: ClimbingRoute):
    return route.length

def order_by_difficulty(route: ClimbingRoute):
    return route.grade

def sort_by_length(routes: list):
    return sorted(routes, key=order_by_length, reverse=True)

def sort_by_difficulty(routes: list):
    l1 = sorted(routes, key=order_by_length, reverse=True)
    l2 = sorted(l1, key=order_by_difficulty, reverse=True)
    return l2

# You can test your function by calling it within the following block
if __name__ == "__main__":
    # r1 = ClimbingRoute("Edge", 38, "6A+")
    # r2 = ClimbingRoute("Smooth operator", 11, "7A")
    # r3 = ClimbingRoute("Synchro", 14, "8C+")
    # r4 = ClimbingRoute("Small steps", 12, "6A+")
    # routes = [r1, r2, r3, r4]
    # for route in sort_by_difficulty(routes):
    #     print(route)

    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])
    for route in sort_by_difficulty(reply):
        print(route)



# Answers!!!
# def sort_by_length(routes: list):
#     def length_order(route):
#         return route.length
 
#     return sorted(routes, key=length_order, reverse=True)
 
# def sort_by_difficulty(routes: list):
#     def difficulty_order(route):
#         return (route.grade, route.length)
 
#     return sorted(routes, key=difficulty_order, reverse=True)