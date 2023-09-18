n = int(input())
a = []
for _ in range(n):
    name = input()
    ac, submit = list(map(int, input().split()))
    a.append((name, ac, submit))
a.sort(key=lambda x: (-x[1], x[2], x[0]))
for x in a:
    print(x[0], x[1], x[2])
