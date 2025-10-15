def main():
    n = int(input())
    dp = [[0]*(n+2) for _ in range(n+1)]

    for k in range(0, n+2):
        dp[0][k] = 1
    for j in range(0, n+1):
        for k in range(1, n+1):
            dp[j][k] = 0
            for i in range(1, min(j, k)+1):
                dp[j][k] += dp[j-i][i-1]
    print(dp[n][n])
    return 0


if __name__ == "__main__":
    main()