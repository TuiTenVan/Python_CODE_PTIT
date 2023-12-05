class ThiSinh:
    def __init__(self, ma, name, lythuyet, thuchanh):
        self.ma = ma
        self.name = name
        self.thuchanh = thuchanh
        self.lythuyet = lythuyet
    def trungbinh(self):
        return (self.thuchanh + self.lythuyet) / 2
    def check(self):
        x = self.trungbinh()
        if x > 9.5:
            return "XUAT SAC"
        elif x >= 8:
            return "DAT"
        elif x >= 5:
            return "CAN NHAC"
        else:
            return "TRUOT"
    def __str__(self):
        return f'{self.ma} {self.name} {self.trungbinh():.2f} {self.check()}'
if __name__ == '__main__':
    t = int(input())
    list = []
    for j in range(0, t):
        name = input()
        s = input()
        lythuyet = 0
        if float(s) > 10: lythuyet = float(s) / 10
        else: lythuyet = float(s)
        y = input()
        thuchanh = 0
        if float(y) > 10: thuchanh = float(y) / 10
        else: thuchanh = float(y) 
        list.append(ThiSinh("TS0" + str(j + 1), name, lythuyet, thuchanh))
    a = sorted(list, key=lambda x: - x.trungbinh())
    for i in a:
        print(i)
        
