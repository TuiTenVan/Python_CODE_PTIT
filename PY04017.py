class VanToc:
    def __init__(self, ma, name, add, end):
        self.name = name
        self.add = add
        self.end = end
        self.ma = ma
    def getMa(self):
        result = ""
        names = self.name.split()
        adds = self.add.split()
        for item in adds:
            result += item[0]
        for item in names:
            result += item[0]
        return result

    def calc(self):
        gio = int(self.end[0])
        phut = int(self.end[2:])
        x = (gio - 6) * 60 + phut
        return (120000 / x) * 60 / 1000
    def __str__(self):
        return f'{self.getMa()} {self.name} {self.add} {round(self.calc())} {"Km/h"}'
if __name__  == "__main__":
    t = int(input())
    list = []
    for _ in range(t):
        name = input()
        add = input()
        end = input()
        list.append(VanToc("", name, add, end))
    list.sort(key=lambda x : -x.calc())
    for i in list:
        print(i)