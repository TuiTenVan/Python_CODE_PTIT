for _ in range(int(input())):
    k = int(input())
    s = input()
    tmp = int(s, 2)
    if k == 2:
        print(s)
    elif k == 4:
        result = ""
        while tmp > 0:
            result = str(tmp % 4) + result
            tmp //= 4
        print(result)
    elif k == 8:
        print(oct(tmp)[2:])
    elif k == 16:
        print(hex(tmp)[2:])
