with open('SOTAY.txt') as file_A:
    lines = file_A.readlines()
contacts = []
for line in lines:
    parts = line.strip()
    s = ""
    if not line.startswith('Ngay ') and not line.startswith('0'):
        s += parts + ": "
for line in lines:
    parts = line.strip()
    s = ""
    if line.startswith('0'):
        s += parts + " "
for line in lines:
    parts = line.strip()
    s = ""
    if line.startswith('Ngay '):
        s += parts[5:] + "\n"
with open('DIENTHOAI.txt', 'w', encoding='utf-8') as dienthoai_file:
    

        



