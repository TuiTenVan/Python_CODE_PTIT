import math
from decimal import Decimal, getcontext

def find_first_two_digits(n):
    # Thiết lập ngữ cảnh chính xác cho tính toán decimal
    getcontext().prec = 102   # Số chữ số thập phân tối đa

    # Tính (2 + √3)^n
    result = Decimal(2 + math.sqrt(3)) ** n

    # Lấy hai chữ số đầu tiên trước dấu phẩy
    result_str = str(result)
    decimal_index = result_str.index('.')
    first_two_digits = result_str[decimal_index - 2 : decimal_index]

    return first_two_digits

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    n = int(input())
    answer = find_first_two_digits(n)
    print(answer)
