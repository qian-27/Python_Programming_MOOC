# Exercise 1
from math import sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_from_origo(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"


class ComparablePoint(Point):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)

    # Equal to
    def __eq__(self, another):
        # if self.x == another.x and self.y == another.y:
        #     return True
        return self.x == another.x and self.y == another.y

    # Greater than
    def __gt__(self, another):
        return self.distance_from_origo() > another.distance_from_origo()

    # Addition
    def __add__(self, another):
        new_x = self.x + another.x
        new_y = self.y + another.y
        return Point(new_x, new_y)


# You can test your function by calling it within the following block
# if __name__ == "__main__":
#     p1 = ComparablePoint(1, 0)
#     p2 = ComparablePoint(0, 1)
#     p3 = ComparablePoint(1, 0)
#     p4 = ComparablePoint(0, 0)

#     print(p1)
#     print(p2)
#     print(p3)
#     print(p4)

#     print(p1 == p2)
#     print(p1 == p3)
#     print(p1 > p4)
#     print(p4 > p1)
#     print(p1 + p2)




