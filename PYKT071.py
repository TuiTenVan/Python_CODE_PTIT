import struct

def check(n):
    s = str(n)
    if len(s) < 2:
        return False
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True

with open('DATA1.in', 'rb') as file1, open('DATA2.in', 'rb') as file2:
    list1 = [struct.unpack('i', line)[0] for line in file1]
    list2 = [struct.unpack('i', line)[0] for line in file2]

a = [0] * 100000
b = [0] * 100000

list1.sort()
list2.sort()

for i in list1:
    if check(i):
        a[i] += 1

for i in list2:
    if check(i) and a[i] > 0:
        b[i] += 1

for i in range(100000):
    if a[i] > 0 and b[i] > 0:
        print(f'{i} {a[i]} {b[i]}')
