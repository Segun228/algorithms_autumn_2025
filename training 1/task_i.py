import sys
def main():
    x, y = map(int, sys.stdin.readline().split())
    f, g = map(int, sys.stdin.readline().split())
    hor = abs(x - f)
    vert = abs(y - g)

    if hor != 0:
        hor -= 1

    if vert != 0:
        vert -= 1
    res = 3 * (hor + vert) + 1
    if x == f or y == g:
        res -= 1
    print(res)
    return 0


if __name__ == "__main__":
    main()