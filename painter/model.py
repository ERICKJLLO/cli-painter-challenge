import matplotlib.pyplot as plt
import pickle


class Point:
    def __init__(self,x,y) -> float:
        self.x = x
        self.y = y

class Circle:
    
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self)-> float:#falta agregar
        pass
    
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str: #falta agregar
        # Circle with center at (x, y) and radius r
        pass

class Triangle:
   
    def __init__(self, point_1, point_2, point_3) -> Point:
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
   
    def area(self) -> float:#falta agregar
        pass
   
    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()
   
    def __str__(self) -> str: #falta agregar
        # Triangle with vertices at (x1, y1), (x2, y2) and (x3, y3)
    
        pass

class Resctangle:

    def __init__(self, point_1, point_2) -> Point:
        self.point_1 = point_1
        self.point_2 = point_2
       
        pass
    
    def area(self) -> float:#falta agregar
        pass
    
    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:#falta agregar
        # Rectangle with vertices at (x1, y1) and (x2, y2)
        pass
class Painter:

FILE = ".painter"

def __init__(self) -> None:
    self.shapes: list = []
    self._load()

def _load(self) -> None:
    try:
        with open(Painter.FILE, "rb") as f:
            self.shapes = pickle.load(f)
    except (EOFError, FileNotFoundError):
        self.shapes = []

def _save(self) -> None:
    with open(Painter.FILE, "wb") as f:
        pickle.dump(self.shapes, f)

def add_shape(self, shape) -> None:
    self.shapes.append(shape)
    self._save()

def total_area(self) -> float:
    return sum(shape.area() for shape in self.shapes)

def clear(self) -> None:
    self.shapes = []
    self._save()