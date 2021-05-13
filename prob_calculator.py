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
            try:
                randItem = random.choice(self.contents)
                listOut.append(randItem)
                self.contents.remove(randItem)
            except:
                pass
        return listOut

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    total = 0
    for num in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        for count in expected_balls:
            if expected_balls[count] > drawn.count(count):
                total -= 1
                break
        total += 1
    return total/num_experiments