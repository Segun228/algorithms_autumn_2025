from collections import deque

def main():
    n, m = map(int, input().split())

    field = []
    for i in range(n):
        row = list(map(int, input().split()))
        field.append(row)

    indegree = [[0] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    graph = [[] for _ in range(n * m)]

    for i in range(n):
        for j in range(m):
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == field[i][j] + 1:

                    idx_from = i * m + j
                    idx_to = ni * m + nj
                    graph[idx_from].append(idx_to)
                    indegree[ni][nj] += 1

    dp = [[1] * m for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(m):
            if indegree[i][j] == 0:
                queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        idx = i * m + j

        for next_idx in graph[idx]:
            ni, nj = next_idx // m, next_idx % m
            dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)
            indegree[ni][nj] -= 1
            if indegree[ni][nj] == 0:
                queue.append((ni, nj))

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dp[i][j])
    print(ans)
    return 0

if __name__ == "__main__":
    main()