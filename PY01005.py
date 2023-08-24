x = input()
cnt4 = 0
cnt7 = 0
for i in x:
    if i == '4':
        cnt4 += 1
    elif i == '7':
        cnt7 += 1
k = cnt4 + cnt7
if(k == 4 or k == 7):
    print("YES")
else:
    print("NO")