import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.red = args.get('red')
        self.blue = args.get('blue')
        self.contents = []
        for r in range(self.red):
            self.contents.append("red")
        for b in range(self.blue):
            self.contents.append("blue")

    def draw(self, numNeed):
        listOut = []
        for cnt in range(numNeed):
            randItem = random.choice(self.contents)
            listOut.append(randItem)
            self.contents.remove(randItem)
        return listOut


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):