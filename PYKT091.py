from collections import *
def check(s):
    return s == s[::-1]
with open("VANBAN.ini", "r") as file:
    s = file.read()
ans = {}
max_len = 0
lines = s.split()
for line in lines:
    max_len = max(max_len, len(line))
cnt = 0
for line in lines:
    if check(line) and max_len == len(line):
        ans = [line]
        if line not in ans:
            ans[line] = 1
        else:
            ans[line] += 1
ans.sort(key=)
