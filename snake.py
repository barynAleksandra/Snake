from turtle import Turtle, Screen, turtles
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.turtles = []
        self.create_a_snake()
        self.head = self.turtles[0]


    def create_a_snake(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.color('white')
            turtle.penup()
            turtle.setx(-20*i)
            self.turtles.append(turtle)

    
    def exend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[-1].position())
        self.turtles.append(new_segment)


    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_a_snake()
        self.head = self.turtles[0]


    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
        

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)