from datetime import datetime

class DanhSach:
    i = 1

    def __init__(self, day, time, phong):
        self.ma = "C" + str(DanhSach.i).zfill(3)
        DanhSach.i += 1
        self.time = time
        self.phong = phong
        self.day = day
        self.day1 = datetime.strptime(day, "%d/%m/%Y")

    def get_day(self):
        return int(self.day1.timestamp() / (60 * 60 * 24))

    def total_time(self):
        x, y = map(int, self.time.split(':'))
        return x * 60 + y

    def __str__(self):
        return f"{self.ma} {self.day} {self.time} {self.phong}"


if __name__ == "__main__":
    with open("CATHI.in", "r") as file:
        n = int(file.readline().strip())
        danh_sach_list = []
        for _ in range(n):
            day = file.readline().strip()
            time = file.readline().strip()
            phong = file.readline().strip()
            danh_sach = DanhSach(day, time, phong)
            danh_sach_list.append(danh_sach)

    danh_sach_list.sort(key=lambda danh_sach: (danh_sach.get_day(), danh_sach.total_time()))

    for danh_sach in danh_sach_list:
        print(danh_sach)
