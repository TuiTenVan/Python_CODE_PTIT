s1 = input().lower().split(' ')
s2 = input().lower().split(' ')
list1 = []
list2 = []
for i in s1:
    if not i in list1:
        list1.append(i)
for i in s2:
    if not i in list1:
        list1.append(i)
for i in s1:
    if (i in s2) and not i in list2:
        list2.append(i)
list1.sort()
list2.sort()
for i in list1:
    print(i, end=" ")
print()
for i in list2:
    print(i, end=" ")