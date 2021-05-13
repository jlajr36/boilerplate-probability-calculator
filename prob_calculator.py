import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.contents = []
        for arg in args:
            for count in range(args[arg]):
                self.contents.append(arg)
    def draw(self, numNeed):
        listOut = []
        for cnt in range(numNeed):
            randItem = random.choice(self.contents)
            listOut.append(randItem)
            self.contents.remove(randItem)
        return listOut

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass