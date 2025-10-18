import sys
def check_k(k, a, b, n):
    prefix_a = [0] * (n + 1)
    prefix_b = [0] * (n + 1)
    for i in range(n):
        prefix_a[i + 1] = prefix_a[i] + a[i]
        prefix_b[i + 1] = prefix_b[i] + b[i]
    for i in range(n):
        left = max(0, i - k)
        right = min(n, i + k + 1)
        food = prefix_b[right] - prefix_b[left]
        if prefix_a[i + 1] > food:
            return False
    return True


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) > sum(b):
        print(-1)
        return
    left, right = 0, n - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if check_k(mid, a, b, n):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
    return 0

if __name__ == "__main__":
    main()