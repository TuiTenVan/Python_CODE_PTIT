n = int(input())
m = {}
for j in range(n) :
    s = ''
    for i in input().lower() + ' ' :
        if (i >= 'a' and i <= 'z'): s += i
        else :
            if(s != '') :
                if s in m : m[s] += 1
                else : m[s] = 1
                s = ''
m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for i in m :
    print(i[0], i[1])