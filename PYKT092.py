from math import *
class ThiSinh:
    def __init__(self, id, name, diem, dtoc, kvuc):
        self.id = id
        self.name = name
        self.diem = diem
        self.dtoc = dtoc
        self.kvuc = kvuc
    def uutien(self):
        t = self.kvuc
        k = self.dtoc
        total = 0
        if t == 1: total += 1.5
        elif t == 2: total += 1
        if k == "Kinh": return total
        else: 
            total += 1.5
            return total
    def get(self):
        return self.diem + self.uutien()
    def __str__(self):
        res = self.get()
        if res >= 20.5: s = "Do"
        else: s = "Truot"
        return f'{self.id} {self.name} {res} {s}'
if __name__ == "__main__":
    a = []
    t = int(input())
    for i in range(t):
        name = ' '.join(input().title().split())
        diem = float(input())
        dtoc = input()
        kvuc = int(input())
        a.append(ThiSinh('TS{:02d}'.format(i +1), name, diem, dtoc, kvuc))
    a.sort(key = lambda x : -x.get())
    for x in a:
        print(x)
