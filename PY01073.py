def next_permutation(s):
    n = len(s)
    s = list(s)
    i = n - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while s[j] <= s[i]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = list(reversed(s[i + 1:]))
        return ''.join(s)
    return None

s = input()
while s is not None:
    print(s)
    s = next_permutation(s)
    if s is None:
        break
