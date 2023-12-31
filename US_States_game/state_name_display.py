from turtle import Turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"


class StateName(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.state = state
        self.was_guessed = False
        self.display_name()

    def display_name(self, font=FONT):
        self.clear()
        self.write(arg=self.state, font=font, align=ALIGNMENT)
    #
    # def is_answer(self, answer):
    #     if self.state.lower() == answer:
    #         self.was_guessed = True
    #         return True
    #     else:
    #         pass
