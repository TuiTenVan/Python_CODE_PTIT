n = int(input())
list = []
a = {}
check = True
for _ in range(0, n - 1):
    row = map(int, input().split())
    if row[0] == row[1]: 
        check = False
        break
    a.get(row)
if check == False:
    print("No")
else: 
    for i in range(1, n + 1):
        list.append(i)
