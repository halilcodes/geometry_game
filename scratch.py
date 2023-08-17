from random import randint


# rectangle = turtle.Turtle()

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        pass

    def falls_in_rectangle(self, check) -> bool:
        if check.p1.x < self.x < check.p2.x \
                and check.p1.y < self.y < check.p2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, p1: Point, p2: Point):
        # initial corner points
        self.p1 = p1
        self.p2 = p2
        # remaining 2 points
        self.p3 = Point(self.p1.x, self.p2.y)
        self.p4 = Point(self.p2.x, self.p3.y)

    def draw(self, bg="white"):
        pass

    def area(self) -> float:
        height = abs(round(self.p2.y - self.p1.y, 2))
        length = abs(round(self.p2.x - self.p1.x, 2))
        return height * length


if __name__ == "__main__":
    rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                          Point(randint(10, 19), randint(10, 19)))

    # Print rectangle coordinates
    print("Rectangle Coordinates: ",
          rectangle.p1.x, ",",
          rectangle.p1.y, "and",
          rectangle.p2.x, ",",
          rectangle.p2.y)

    # Get point and area from user
    user_point = Point(int(input("Guess x: ")), int(input("Guess y: ")))
    user_area = float(input("Guess rectangle area: "))

    # Print out the game result
    print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
    print("Your area was off by: ", rectangle.area() - user_area)
    print(rectangle.area())
