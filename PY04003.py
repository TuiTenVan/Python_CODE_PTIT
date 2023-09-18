class PhanSo:
    def __init__ (self, tu, mau):
        self.tu = tu
        self.mau = mau

    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
   
    def toi_gian(self):
        v = self.gcd(self.tu, self.mau)
        self.tu = self.tu // v
        self.mau = self.mau // v

    def __str__(self):
        self.toi_gian()
        return f"{self.tu}/{self.mau}"
    
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    k = PhanSo(tu, mau)
    print(k)