from turtle import Screen, Turtle
from random import randint


class Point(Turtle):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def draw(self, color="black"):
        self.penup()
        self.goto(self.x*2, self.y*2)
        self.color(color)
        self.dot(size=20)

    def falls_in_rectangle(self, check) -> bool:
        if check.p1.x < self.x < check.p2.x \
                and check.p1.y < self.y < check.p2.y:
            return True
        else:
            return False


class Rectangle(Turtle):
    def __init__(self, p1: Point, p2: Point):
        super().__init__()
        # initial corner points
        self.p1 = p1
        self.p2 = p2
        # remaining 2 points
        self.p3 = Point(self.p1.x, self.p2.y)
        self.p4 = Point(self.p2.x, self.p1.y)

    def draw(self, bg="green"):
        print(f"{self.p1.x=}--{self.p1.y=}")
        print(f"{self.p2.x=}--{self.p2.y=}")
        print(f"{self.p3.x=}--{self.p3.y=}")
        print(f"{self.p4.x=}--{self.p4.y=}")
        self.color(bg)
        # self.speed('fastest')

        self.penup()
        self.goto(self.p1.x*2, self.p1.y*2)
        self.pendown()

        self.begin_fill()
        self.goto(self.p3.x*2, self.p3.y*2)
        self.goto(self.p2.x*2, self.p2.y*2)
        self.goto(self.p4.x*2, self.p4.y*2)
        self.end_fill()
        self.hideturtle()

    def area(self) -> float:
        height = abs(round(self.p2.y - self.p1.y, 2))
        length = abs(round(self.p2.x - self.p1.x, 2))
        return height * length


if __name__ == "__main__":
    rectangle = Rectangle(Point(randint(0, 9)*10, randint(0, 9)*10),
                          Point(randint(10, 19)*10, randint(10, 19)*10))

    # Print rectangle coordinates
    print("Rectangle Coordinates: ",
          rectangle.p1.x, ",",
          rectangle.p1.y, "and",
          rectangle.p2.x, ",",
          rectangle.p2.y)

    # Get point and area from user
    user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
    user_area = float(input("Guess rectangle area: "))

    # Print out the game result
    print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
    print("Your area was off by: ", rectangle.area() - user_area)
    print(rectangle.area())

    screen = Screen()

    rectangle.draw()
    user_point.draw()

    screen.exitonclick()

