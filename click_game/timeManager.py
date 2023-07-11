import time

class gameTime() :
    def __init__(self) :
        self.start = time.time_ns()

    
    def timePassed(self) :
        now = time.time_ns()

        return round((now - self.start)/1000000000, 3)


