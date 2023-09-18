
def count(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count

N, K = map(int, input().split())
A = list(map(int, input().split()))

arr = [count(x) for x in A]
A.sort(key=lambda x: (-arr[A.index(x)], x), reverse=True)

selected_numbers = A[:K]
ans = 1
for i in selected_numbers:
    ans *= i
result = count(ans)
print(result)
