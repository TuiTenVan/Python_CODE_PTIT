import math
n = int(input())
value = input().split()
values = sorted(map(int, value))
for i in range(0, len(values) - 1):
    for j in range(i + 1, len(values)):
        if math.gcd(values[i], values[j]) == 1:
            print(values[i], values[j])

