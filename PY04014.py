class BangDiem:
    def __init__(self, id,  name, tb):
        self.id = id
        self.name = name
        self.tb = tb
    def check(self):
        if self.tb >= 9:
            return "XUAT SAC"
        elif self.tb >= 8:
            return "GIOI"
        elif self.tb >= 7:
            return "KHA"
        elif self.tb >= 5:
            return "TB"
        else:
            return "YEU"
    def getTB(self):
        return self.tb
    def __str__(self):
        # x = round(self.tb * 100, 1)
        # self.tb = x / 100
        return f'{self.id} {self.name} {round(self.tb + 0.01, 1)} {self.check()}'
    
if __name__ == "__main__":
    t = int(input())
    list1 = []
    for j in range(t):
        name = input()
        a = list(map(float, input().split()))
        tb = 0
        tb += a[0] * 2 + a[1] * 2
        for i in range(2, len(a)):
            tb += a[i]
        tb /= 12
        list1.append(BangDiem('HS{:02d}'.format(j + 1), name, tb))
    arr = sorted(list1, key=lambda x: - x.getTB())
    for i in arr:
        print(i)
