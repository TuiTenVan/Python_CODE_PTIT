n = input()
cnt = 0
while len(n) > 1:
    cnt += 1
    sum = 0
    for i in range(0, len(n)):
        sum += ord(n[i]) - ord('0')
    n = str(sum)
print(cnt)