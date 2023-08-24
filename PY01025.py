s = str(input())
x = reversed(s)
cnt = 0
res = ""
for i in x :
    cnt += 1
    res += i
    if cnt % 3 == 0 and cnt != len(s):
        res += ','
print(''.join(reversed(res)))
