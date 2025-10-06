def solve(a, b, c, v0, v1, v2):
    times = []
    times.append(a / v0 + c / v1 + b / v2)
    times.append(b / v0 + c / v1 + a / v2)
    times.append(a / v0 + a / v1 + b / v0 + b / v1)
    times.append(b / v0 + b / v1 + a / v0 + a / v1)
    times.append(b / v0 + c / v0 + c / v1 + b / v2)
    times.append(a / v0 + c / v0 + c / v1 + a / v2)

    times.append(b / v0 + c / v0 + a / v1 + b / v0 + b / v1)
    times.append(a / v0 + c / v0 + b / v1 + a / v0 + a / v1)

    times.append(b / v0 + c / v0 + b / v1 + c/v1 + b / v0 + b / v1)
    times.append(a / v0 + c / v0 + a / v1 + c/v1 + a / v0 + a / v1)
    return min(times)

def main():
    a, b, c, v0, v1, v2 = map(int, input().split())
    print(solve(a, b, c, v0, v1, v2))
    return 0

if __name__ == "__main__":
    main()