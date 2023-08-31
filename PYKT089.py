n = int(input())
a = list(map(int, input().split()))
a1 = []
a2 = []
for i in a:
    if i % 2 == 0:
        a1.append(i)
    else:
        a2.append(i)
arr1 = sorted(a1)
arr2 = sorted(a2, reverse=True)
ans = []
le = 0
chan = 0
for i in a:
    if i % 2 != 0:
        ans.append(arr2[le])
        le += 1
    else:
        ans.append(arr1[chan])
        chan += 1
print(" ".join(map(str, ans)))
