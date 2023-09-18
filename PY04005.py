import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x0 = self.x - other.x
        y0 = self.y - other.y
        return math.sqrt(x0 * x0 + y0 * y0)
    
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def output(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(a + b <= c or a + c <= b or b + c <= a):
            print("INVALID")
        else:
            print('{:.3f}'.format(a + b + c))
if __name__ == "__main__":
    list = []
    t = int(input())
    for _ in range(t):
        list += [float(i) for i in input().split()]
        i = 0
    while i <= len(list) - 5:
        x = Triangle(Point(list[i], list[i + 1]), Point(list[i + 2], list[i + 3]), Point(list[i + 4], list[i + 5]))
        x.output()
        i += 6
