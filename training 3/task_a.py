from math import sqrt

def check_valid(l, a, b, s):
    if (l-a)*(l-b) >= s:
        return True
    return False


def check_condition(l, a, b, s):
    if l > max(a, b) and (l - a) * (l - b) == s:
        return True
    return False


def main():
    a, b, s = map(int, input().split())
    lower = max(a, b) + 1
    upper = a + b + int(sqrt(s)) + 100
    while lower <= upper:
        middle = (lower + upper)//2
        if check_valid(middle, a, b, s):
            upper = middle - 1
        else:
            lower = middle + 1
    if check_condition(lower, a, b, s):
        print(lower)
    else:
        print(-1)
    return 0


if __name__ == "__main__":
    main()