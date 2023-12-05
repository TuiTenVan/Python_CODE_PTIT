t = int(input())
lucbat = []
thatngon = []
for i in range(t):
    s = input().split()
    cnt1 , cnt2 = 0, 0
    if(len(lucbat) == 0 or len(s) == 8):
        cnt1 = 1
    lucbat.append(s)
    