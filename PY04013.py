class TinhToan:
    def __int__(self, tram, begin, end, cnt):
        self.tram = tram
        self.begin = begin
        self.end = end
        self.cnt = cnt
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        tram = input()
        begin = input()
        end = input()
        cnt = int(input())