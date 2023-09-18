import re

def chuan__hoa(s):
    s = s.lower()
    s = s[0].upper() + s[1:]
    s = ' '.join(s.split())
    s = re.sub(r'\s+([.!?])', r'\1', s)
    if not s.endswith(('.', '!', '?')):
        s += '.'
    return s

if __name__ == "__main__":
    while True:
        try:
            line = input()
            print(chuan__hoa(line))
        except EOFError:
            break
