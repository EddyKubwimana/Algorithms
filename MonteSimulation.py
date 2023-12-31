import random
class Roulette(object):

    def __init__(self):
        self.pockets = []
        for i in range(37):
            self.pockets.append(i)

        self.pockets0dd = len(self.pockets)-1
        self.ball = None
    
    def spin(self):
        '''Spin the the roulette and return the chosen pocket'''
        self.ball = random.choice(self.pockets)
        return self.ball


    def betPocket(self, pocket, amt):
        '''Allow to bet and return if the loss or win of the player'''
        if str(self.ball) == str(pocket):
            return amt*self.pockets0dd
        
        return -amt
    

    def __str__(self):
        return "Fair roulette"



# --------------------------------Testing--------------------------------------------#

bet= Roulette()
print(bet.spin())
for i in range(40):
  print(bet.betPocket(i, 20), end = " ")

    

