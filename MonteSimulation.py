import random
class Roulette(object):

    def __init__(self):
        self.pockets = []
        for i in range(37):
            self.pockets.append(i)

        self.pockets0dd = len(self.pockets)-1
        self.ball = None
    
    def spin(self):
        self.ball = random.choice(self.pockets)


    def betPocket(self, pocket, amt):
        if self.ball == pocket:
            return amt*pocket
        
        return -amt
    

    def __str__(self)
        return "Fair roulette"

    

    