import math
s = input()
s = s.lower()
x = s[-3:]
if x == ".py":
    print("yes")
else:
    print("no")