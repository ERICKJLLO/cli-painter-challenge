import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y) -> float:
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self)-> float:
        pass
    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        pass

class Triangle:
    def __init__(self, point_1, point_2, point_3) -> Point:
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
    
