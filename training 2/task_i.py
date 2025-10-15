def dfs(n, m, a, i, j, dp, directions):
    if dp[i][j] != 0:
        return dp[i][j]
    best = 1
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and a[ni][nj] == a[i][j] + 1:
            best = max(best, 1 + dfs(n, m, a, ni, nj, dp, directions))
    dp[i][j] = best
    return best


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(0, n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ans = 0
    for i in range(0, n):
        for j in range(0, m):
            ans = max(ans, dfs(n, m, a, i, j, dp, directions))
    print(ans)
    return 0


if __name__ == "__main__":
    main()
