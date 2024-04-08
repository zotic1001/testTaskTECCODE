class Point:
    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, var):
        self._x = var

    @y.setter
    def y(self, var):
        self._y = var

    def calculate_distance(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    
