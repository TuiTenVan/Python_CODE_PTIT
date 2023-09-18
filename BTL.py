class Pair:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2

    def first(self):
        return self.t1

    def second(self):
        return self.t2


def main():
    with open("SOTAY.in", "r") as file:
        lines = file.readlines()

    t = int(lines[0])
    lines = lines[1:]

    for _ in range(t):
        s = lines[_].strip()
        st = []
        ans = 0
        n = len(s)
        f = [0] * n
        for i in range(n):
            if s[i] == ')' and st and st[-1].first() == '(':
                f[i] = f[i - 1]
                if st[-1].second() != 0:
                    f[i] += f[st[-1].second() - 1]
                f[i] += 2
                st.pop()
            else:
                st.append(Pair(s[i], i))
            ans = max(ans, f[i])
        print(ans)


if __name__ == "__main__":
    main()
