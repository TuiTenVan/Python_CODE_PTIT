from datetime import datetime

class HoaDon:
    def __init__(self, ma, name, sophong, nhan, tra, phatsinh):
        self.ma = ma
        self.name = name
        self.nhan = nhan
        self.tra = tra
        self.phatsinh = phatsinh
        self.sophong = sophong
    def checkTime(self):
        nhan = datetime.strptime(self.nhan, "%d/%m/%Y")
        tra = datetime.strptime(self.tra, "%d/%m/%Y")
        return (tra - nhan).days + 1
    def Tien(self):
        x = int(self.sophong[0])
        if x == 1:
            return 25
        elif x == 2:
            return 34
        elif x == 3:
            return 50
        else:
            return 80
    def TongTien(self):
        return self.Tien() * self.checkTime() + self.phatsinh
    def __str__(self):
        return f'{self.ma} {self.name} {self.sophong} {self.checkTime()} {self.TongTien()}'
if __name__== '__main__':
    t = int(input())
    list = []
    for i in range(t):
        name = input().strip()
        sophong = input().strip()
        nhan = input().strip()
        tra = input().strip()
        phatsinh = int(input().strip())
        list.append(HoaDon('KH{:02d}'.format(i + 1), name, sophong, nhan, tra, phatsinh))
    list.sort(key=lambda x: -x.TongTien())
    for i in list:
        print(i)