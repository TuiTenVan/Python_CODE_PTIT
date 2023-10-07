def count_substrings(N, M, s):
    len_s = len(s)
    
    # Tạo một mảng prefix để lưu số lượng prefix của xâu s
    prefix = [0] * (len_s + 1)
    for i in range(1, len_s + 1):
        prefix[i] = prefix[i - 1] + (s[i - 1] == s[0])
    
    # Tính số lượng xâu con t chứa xâu s
    result = 0
    for i in range(1, N + 1):
        result = (result + prefix[min(i, len_s)]) % M
    
    return result

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    s = input().strip()
    
    result = count_substrings(N, M, s)
    print(result)
