t = int(input())

he4 = {
    "00": "0",
    "01": "1",
    "10": "2",
    "11": "3",
}

he8 = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
}

he16 = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}

while t!=0:
    t-=1
    n = int(input())
    s = input().strip()

    res = ""
    if n==2: print(s)
    elif n==4:
        while len(s)%2!=0: s = "0" + s
        bg = 0; ed = 2
        while bg!=len(s):
            z = s[bg:ed]
            bg+=2
            ed+=2
            res += he4[z]
        print(res)
    elif n==8:
        while len(s)%3!=0: s = "0" + s
        bg = 0; ed = 3
        while bg!=len(s):
            z = s[bg:ed]
            bg+=3
            ed+=3
            res += he8[z]
        print(res)
    elif n==16:
        while len(s)%4!=0: s = "0" + s
        bg = 0; ed = 4
        while bg!=len(s):
            z = s[bg:ed]
            bg+=4
            ed+=4
            res += he16[z]
        print(res)