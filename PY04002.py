class Rectangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        if self.x <= 0 or self.y <= 0:
            return 0
        else:
            return (self.x + self.y) * 2

    def area(self):
        if self.x <= 0 or self.y <= 0:
            return 0
        else:
            return self.x * self.y

    def color(self):
        res = ""
        k = self.z.lower()
        res += k[0].upper()
        for i in range(1, len(self.z)):
            res += k[i].lower()
        return res

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    if r.area() == 0 or r.perimeter() == 0:
        print("INVALID")
    else:
        print(r.perimeter(), r.area(), r.color())
