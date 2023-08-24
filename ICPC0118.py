t = int(input())
for i in range(t):
    d, m = input().split()
    d = int(d)
    m = int(m)
    if m == 1:
        if(d <= 19 and d >= 1):
            print("Ma Ket")
        else:
            print("Bao Binh")
    elif m == 2:
        if(d <= 18 and d >= 1):
            print("Bao Binh")
        else:
            print("Song Ngu")
    elif m == 3:
        if(d <= 20 and d >= 1):
            print("Song Ngu")
        else:
            print("Bach Duong")
    elif m == 4:
        if(d <= 19 and d >= 1):
            print("Bach Duong")
        else:
            print("Kim Nguu")
    elif m == 5:
        if(d <= 20 and d >= 1):
            print("Kim Nguu")
        else:
            print("Song Tu")
    elif m == 6:
        if(d <= 20 and d >= 1):
            print("Song Tu")
        else:
            print("Cu Giai")
    elif m == 7:
        if(d <= 22 and d >= 1):
            print("Cu Giai")
        else:
            print("Su Tu")
    elif m == 8:
        if(d <= 22 and d >= 1):
            print("Su Tu")
        else:
            print("Xu Nu")
    elif m == 9:
        if(d <= 22 and d >= 1):
            print("Xu Nu")
        else:
            print("Thien Binh")
    elif m == 10:
        if(d <= 22 and d >= 1):
            print("Thien Binh")
        else:
            print("Thien Yet")
    elif m == 11:
        if(d <= 22 and d >= 1):
            print("Thien Yet")
        else:
            print("Nhan Ma")
    elif m == 12:
        if(d <= 21 and d >= 1):
            print("Nhan Ma")
        else:
            print("Ma Ket")
    