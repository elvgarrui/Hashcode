
class GeneralInfo:
    def __init__(self, R:int, C:int, F:int, N:int, B:int, T:int):
        self.R = R
        self.C = C
        self.F = F
        self.N = N
        self.B = B
        self.T = T


class Ride:
    def __init__(self, i:int, a:int, b:int, x:int, y:int, s:int, f:int):
        self.i = i
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f

    def calculate_distance(self):
        return abs(self.a - self.b) + abs(self.b - self.y)


class Vehicle:
    def __init__(self, i:int, pos_x:int, pos_y:int):
        self.i = i
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rides = []

