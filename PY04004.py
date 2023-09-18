class PhanSo:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
    def __str__(self):
        mau = self.b * self.d
        tu = self.a * self.d + self.c * self.b
        u = self.gcd(tu, mau)
        mau = mau // u
        tu = tu // u
        return f"{tu}/{mau}"
if __name__ == "__main__":
    a,b,c,d = map(int, input().split())
    k = PhanSo(a,b,c,d)
    print(k)