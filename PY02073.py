class data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check(N, X, Y, Z):
    a, q = [-1] * 110, []
    q.append(data(0, 0))
    a[0] = 0
    while len(q) > 0:
        u = q[-1]
        q.pop()
        if u.x + 1 < 110 and (a[u.x + 1] == -1 or a[u.x + 1] > u.y + X):
            a[u.x + 1] = a[u.x] + X
            q.append(data(u.x + 1, u.y + X))
        if u.x - 1 > 0 and (a[u.x - 1] == -1 or a[u.x - 1] > u.y + Y):
            a[u.x - 1] = a[u.x] + Y
            q.append(data(u.x - 1, u.y + Y))
        if u.x * 2 < 110 and (a[u.x * 2] == -1 or a[u.x * 2] > u.y + Z):
            a[u.x * 2] = a[u.x] + Z
            q.append(data(u.x * 2, u.y + Z))

    return a[N]

if __name__ == "__main__":
    t = int(input())
    for z in range(t):
        n = int(input())
        X, Y, Z = map(int, input().split())
        result = check(n, X, Y, Z)
        print(result)
