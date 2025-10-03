import sys
from collections import Counter

def main():
    s = input().strip()
    n = len(s)
    cnt = Counter(s)
    same = 0
    for v in cnt.values():
        same += v * (v - 1) // 2
    total = 1 + n * (n - 1) // 2 - same
    print(total)


if __name__ == '__main__':
    main()

