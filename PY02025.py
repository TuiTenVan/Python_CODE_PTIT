n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a1 = set(a)
b1 = set(b)

intersection = a1.intersection(b1)
giao = sorted(intersection)
for i in giao:
    print(i, end=' ')
print()
only_in_A = a1.difference(b1)
A = sorted(only_in_A)
for i in A:
    print(i, end=' ')
print()
only_in_B = b1.difference(a1)
B = sorted(only_in_B)
for i in B:
    print(i, end=' ')
