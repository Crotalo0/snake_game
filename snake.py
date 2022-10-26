from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self, sleep_timer):
        self.segments = []
        self.create_snake()
        self.sleep_timer = sleep_timer

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.segments[0].color('white')

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('springgreen')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = (self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
            self.segments[seg_num].goto(new_pos)
        self.segments[0].forward(20)

    def move_from_first(self):
        initial = self.segments[0].pos()
        for n in self.segments[1:]:
            temp_initial = n.pos()
            n.goto(initial)
            initial = temp_initial
        self.segments[0].forward(20)

    def border_crossed(self):
        return self.segments[0].xcor() > 310 or self.segments[0].xcor() < -310 or \
               self.segments[0].ycor() > 310 or self.segments[0].ycor() < -310

    def tail_collision(self):
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg.pos()) < 10:
                return True

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    # Movements input -------------------------------
    # def up(self):
    #     if self.segments[0].heading() != 270:
    #         self.segments[0].setheading(90)
    #
    # def left(self):
    #     if self.segments[0].heading() != 0:
    #         self.segments[0].setheading(180)
    #
    # def down(self):
    #     if self.segments[0].heading() != 90:
    #         self.segments[0].setheading(270)
    #
    # def right(self):
    #     if self.segments[0].heading() != 180:
    #         self.segments[0].setheading(0)
    # -----------------------------------------------

    def up(self):
        if self.segments[0].ycor() + 20 != self.segments[1].ycor():
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].ycor() - 20 != self.segments[1].ycor():
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].xcor() - 20 != self.segments[1].xcor():
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].xcor() + 20 != self.segments[1].xcor():
            self.segments[0].setheading(0)
