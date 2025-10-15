from collections import deque

def compute_windsum_mins(A, K):
    n = len(A)
    m = n - K + 1
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + A[i]
    sums = [pref[i+K] - pref[i] for i in range(m)]
    mins = [0] * m
    dq = deque()
    for i in range(n):
        while dq and dq[0] <= i - K:
            dq.popleft()
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()
        dq.append(i)
        if i >= K - 1:
            start = i - K + 1
            mins[start] = A[dq[0]]
    return (sums, mins)


def print_list(a:list)->None:
    for el in a:
        print(el, end =" ")


def main():
    n, k = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    if k > n:
        print(0)
        return
    m = n - k + 1
    sums, mins = compute_windsum_mins(A, k)
    weights = [sums[i] * mins[i] for i in range(m)]
    dp = [0] * m
    take = [False] * m
    for i in range(m):
        take_val = weights[i] + (dp[i-k] if i-k >= 0 else 0)
        skip_val = dp[i-1] if i-1 >= 0 else 0
        if take_val > skip_val:
            dp[i] = take_val
            take[i] = True
        else:
            dp[i] = skip_val
            take[i] = False
    res = []
    i = m - 1
    while i >= 0:
        if take[i]:
            res.append(i + 1)
            i -= k
        else:
            i -= 1
    res.reverse()
    print(len(res))
    if res:
        print_list(res)
    return 0

if __name__ == "__main__":
    main()