import math

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = int(math.sqrt(math.pow(self.x1 - self.x2,2) + math.pow(self.y1 - self.y2, 2)))

    


    