from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.high_score = 0
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
        self.score = 0
        self.update_scoreboard()
        
        
    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Reset the score to zero and update the display."""
        self.score = 0
        self.update_scoreboard()
