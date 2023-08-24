arr = set()
x = 0
while True:
    a = list(map(int, input().split()))
    x += len(a)
    for i in a:
        arr.add(i % 42)
    if x == 10:
        break
print(len(arr))