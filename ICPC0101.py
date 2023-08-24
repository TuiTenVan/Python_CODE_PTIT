
def solve(n , arr):
    stack = [];
    for num in arr:
        if stack and (stack[-1] + num) % 2 == 0:
            stack.pop()
        else:
            stack.append(num)
    return len(stack)
if __name__ == '__main__':
    n = int(input());
    arr = list(map(int, input().split()))
    result = solve(n, arr)
    print(result)

