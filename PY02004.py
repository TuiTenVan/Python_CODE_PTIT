n = int(input())
s = input().split()
cnt = 0
for i in range(0, len(s) - 1):
    if int(s[i]) != int(s[i + 1]):
        cnt += 1
print(cnt)