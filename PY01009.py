s = input()
x1 = 0
x2 = 0
for i in s:
    if i.islower():
        x1 += 1
    else:
        x2 += 1
if x1 >= x2:
    s = s.lower()
    print(s)
else:
    s = s.upper()
    print(s)