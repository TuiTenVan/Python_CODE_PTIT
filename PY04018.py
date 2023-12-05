class GiaoVien:
    def __init__(self, maGV, name, ma, diemTin, diemChuyenMon):
        self.name = name
        self.maGV = maGV
        self.ma = ma
        self.diemTin = diemTin
        self.diemChuyenMon = diemChuyenMon
    def UuTien(self):
        x = int(self.ma[1])
        if x == 1:
            return 2.0
        elif x == 2:
            return 1.5
        elif x == 3:
            return 1.0
        else:
            return 0.0
    def diemTong(self):
        diemTong = self.diemTin * 2 + self.diemChuyenMon + self.UuTien()
        return diemTong
    def checkMon(self):
        s = self.ma[0]
        if(s == 'A'):
            return "TOAN"
        elif(s == 'B'):
            return "LY"
        else:
            return "HOA"
    def __str__(self):
        x = self.diemTong()
        if x >= 18:
            return f'{self.maGV} {self.name} {self.checkMon()} {round(self.diemTong(), 1)} {"TRUNG TUYEN"}'
        else:
            return f'{self.maGV} {self.name} {self.checkMon()} {self.diemTong()} {"LOAI"}'
if __name__ == "__main__":
    t = int(input())
    list = []
    for i in range(t):
        name = input()
        ma = input()
        diemTin = float(input())
        diemChuyenMon = float(input())
        list.append(GiaoVien('GV{:02d}'.format(i + 1), name, ma, diemTin, diemChuyenMon))
    list.sort(key=lambda x : -x.diemTong())
    for i in list:
        print(i)
