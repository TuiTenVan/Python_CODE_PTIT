class ThiSinh:
    def __init__(self, name, birth, mon1, mon2, mon3):
        self.name = name
        self.birth = birth
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
    def tong(self):
        return self.mon1 + self.mon2 + self.mon3
    def __str__(self):
        return f'{self.name} {self.birth} {self.tong():.1f}'
if __name__ == "__main__":
    name = input()
    birth = input()
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input())
    t = ThiSinh(name, birth, mon1, mon2, mon3)
    print(t)

