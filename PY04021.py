from datetime import datetime

class Time:
    def __init__(self, ma, name, vao, ra):
        self.ma = ma
        self.name = name
        self.vao = vao
        self.ra = ra
    def checkTime(self):
        gioVao = int(self.vao[0:2])
        phutVao = int(self.vao[3:])
        gioRa = int(self.ra[0:2])
        phutRa = int(self.ra[3:])
        x = (gioRa * 60 + phutRa) - (gioVao * 60 + phutVao)
        # print(x)
        return x
    def __str__(self):
        k = self.checkTime()
        if k >= 60:
            gio = k // 60
            phut = k - gio * 60
            return f'{self.ma} {self.name} {gio} {"gio"} {phut} {"phut"}'
        else:
            return f'{self.ma} {self.name} {"0 gio"} {k} {"phut"}'
if __name__== '__main__':
    t = int(input())
    list = []
    for i in range(t):
        ma = input().strip()
        name = input().strip()
        vao = input().strip()
        ra = input().strip()
        list.append(Time(ma, name, vao, ra))
    list.sort(key=lambda x: -x.checkTime())
    for i in list:
        print(i)