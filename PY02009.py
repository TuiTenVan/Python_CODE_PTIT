t = int(input())
for i in range(t):
    n = int(input())
    count = {}
    ans = 0
    number = 0
    arr = []
    for j in range(n):
        x = int(input())
        arr.append(x)
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
        if count[x] > ans or (count[x] == ans and x < number):
            ans = count[x]
            number = x
    print(number)

