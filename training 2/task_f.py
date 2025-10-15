from math import inf

def main():
    m = int(input())
    road = [['.', '.', '.']]
    for i in range(m):
        line = input()
        road.append(list(line))
    dp = [[-inf]*3 for _ in range(m+1)]
    coin = 0
    for j in range(3):
        if road[1][j] != 'W':
            dp[1][j] = 1 if road[1][j] == 'C' else 0
        else:
            dp[1][j] = -inf
    for i in range(2, m+1):
        for j in range(3):
            if road[i][j] == 'W':
                dp[i][j] = -inf
                continue
            if road[i][j] == 'C':
                coin = 1
            else:
                coin = 0
            if j == 0:
                dp[i][j] = coin + max(dp[i-1][0], dp[i-1][1])
            elif j == 1:
                dp[i][j] = coin + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
            else:
                dp[i][j] = coin + max(dp[i-1][1], dp[i-1][2])
    print(max([cell for row in dp for cell in row] + [0]))
    return 0



if __name__ == "__main__":
    main()