
class GeneralInfo:
    def __init__(self, R:int, C:int, F:int, N:int, B:int, T:int):
        self.row = R
        self.column = C
        self.float = F
        self.rides = N
        self.bonus = B
        self.steps = T


class Ride:
    def __init__(self, i:int, a:int, b:int, x:int, y:int, s:int, f:int):
        self.i = i
        self.startrow = a
        self.startcolumn = b
        self.finishrow = x
        self.finishcolumn = y
        self.earlystart = s
        self.latestfinish = f

    def calculate_distance(self):
        return abs(self.a - self.b) + abs(self.b - self.y)


class Vehicle:
    def __init__(self, i:int, pos_x:int, pos_y:int):
        self.i = i
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rides = []
