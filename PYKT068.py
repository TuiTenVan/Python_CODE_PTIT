class MonHoc:
    def __init__(self, ma, ten, Hthuc):
        self.ma = ma
        self.ten = ten
        self.Hthuc = Hthuc
    def getMa(self):
        return self.ma
    def __str__(self):
        return f'{self.ma} {self.ten} {self.Hthuc}'
if __name__ == "__main__":
    n = int(input())
    list = []
    for i in range(n):
        ma = input()
        ten = input()
        Hthuc = input()
        list.append(MonHoc(ma, ten, Hthuc))
    list.sort(key=lambda x: x.getMa())
    for i in list:
        print(i)
