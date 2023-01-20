from turtle import Turtle
FONT =  ("Courier", 24, "normal")
ALIGMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0

        with open("data.txt") as file:
            content = file.read()
            self.high_score = int(content)
        
        
        self.hideturtle()
        self.goto(x=0, y=265)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGMENT, FONT)


    def refresh(self):
        self.score += 1
        self.update_scoreboard()
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0    
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGMENT, FONT)
