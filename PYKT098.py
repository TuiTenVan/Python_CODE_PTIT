with open("DATA.in", "r") as file:
   data = file.read().split()
list = []

for i in range(len(data)):
   try:
        if not data[i].isdigit():
            list.append(data[i])
        elif len(data[i]) > 9:
            list.append(data[i])
   except ValueError:
      ValueError("Invalid")
list.sort()
for i in list:
   print(i, end=" ")