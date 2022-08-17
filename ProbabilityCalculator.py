import copy
import random

random.seed(95)

class Hat:
    def __init__(self,**kwargs):
        #Taking inputs and storing them in a list
        self.contents = []
        for ball in kwargs.items():
            for i in range(ball[1]):
                self.contents.append(ball[0])
    
    def draw(self, draw_amount):
        #Randomly pulls balls out of the bag and does not replace them
        drawn_balls = []
        if draw_amount >= len(self.contents):
            return self.contents
        for i in range(draw_amount):
            draw_index = random.randint(0,len(self.contents)-1)
            drawn_balls.append(self.contents[draw_index])
            self.contents.pop(draw_index)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #Carry out draws several times and figure out how many of the total experiments got the expected balls
    successes = 0
    for i in range(num_experiments):
        drawn_balls = copy.deepcopy(hat).draw(num_balls_drawn)
        if is_experiment_successful(drawn_balls,expected_balls):
            successes += 1
    return successes/num_experiments
        
def is_experiment_successful(balls, expected_balls):
    drawn_balls = {}
    for ball in balls:
        if ball in drawn_balls:
            drawn_balls.update({ball:drawn_balls.get(ball)+1})
        else:
            drawn_balls[ball] = 1
    successful = True
    for ball in expected_balls.keys():
        try:
            if drawn_balls.get(ball) >= expected_balls.get(ball):
                pass
            else:
                successful = False
        except:
            successful = False
    return successful

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)


