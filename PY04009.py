class SoPhuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addSoPhuc(self, other):
        x = self.a + other.a
        y = self.b + other.b
        return SoPhuc(x, y)

    def mulPhuc(self, other):
        x = self.a * other.a - self.b * other.b
        y = self.a * other.b + self.b * other.a
        return SoPhuc(x, y)
    def __str__(self):
        if self.b > 0:
            return f'{self.a} + {self.b}i'
        else:
            b_abs = -self.b
            return f'{self.a} - {b_abs}i'

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        s1 = SoPhuc(a, b)
        s2 = SoPhuc(c, d)
        s3 = s1.addSoPhuc(s2)
        s4 = s3.mulPhuc(s1)
        s5 = s3.mulPhuc(s3)
        print(f'{s4}, {s5}')
