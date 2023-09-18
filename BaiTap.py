def calc(x, y):
    try:
        result = x ** y
        return result
    except Exception as e:
        return f"Error: {e}"

try:
    with open('file_A.txt') as file_A, open('file_B.txt') as file_B:
        a = file_A.readlines()
        b = file_B.readlines()
        if len(a) != len(b):
            print("Số lượng dòng trong tệp A và B không giống nhau.")
        else:
            for i in range(len(a)):
                try:
                    x = int(a[i].strip())
                    y = int(b[i].strip())
                    result = calc(x, y)
                    print(f"{x} ** {y} = {result}")
                except ValueError:
                    print(f"Dòng {i+1}: Dữ liệu không phải là số nguyên.")
except FileNotFoundError:
    print("Không tìm thấy tệp A hoặc B.")