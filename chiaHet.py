N, K = map(int, input().split())

ans = 0

for i in range(1, N + 1):
    num = int(''.join(str(j) for j in range(1, i + 1)))
    if num % K == 0:
        ans += 1

print(ans)
