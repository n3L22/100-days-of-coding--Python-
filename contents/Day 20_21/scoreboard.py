from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("100-days-of-coding--Python-\contents\Day 20_21\data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the previous score and write the new score on the screen."""
        self.clear()
        self.write(f"Score: {self.score}    High Score:{self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
        
    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.update_scoreboard()

    # def reset(self):
    #     """Reset the score to zero and update the display."""
    #     self.score = 0
    #     self.update_scoreboard()
