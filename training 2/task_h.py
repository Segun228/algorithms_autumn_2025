from math import sqrt, ceil

def is_prime(n) -> bool:
    if n<2:
        return False
    if n in (2, 3, 5, 7):
        return True
    limit = ceil(sqrt(n))
    for i in range(2, limit+1):
        if n%i == 0:
            return False
    return True


def main():
    N = int(input())
    dp = [False] * (N + 1)
    dp[0] = False
    for i in range(1, N + 1):
        for take in [1, 2, 3]:
            remaining = i - take
            if remaining >= 0 and not is_prime(remaining):
                if not dp[remaining]:
                    dp[i] = True
                    break
    print(1 if dp[N] else 2)


if __name__ == "__main__":
    main()