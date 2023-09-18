import math
t = True
while True:
    n = int(input())
    min_i = 1000000
    max_i = 0
    if n == 0:
       t = False
       break
    while n > 0:
        x = input()
        min_i = min(min_i, int(x))
        max_i = max(max_i, int(x))
        n -= 1
    if min_i != max_i:
        print(min_i, max_i)
    else:
        print("BANG NHAU")
    