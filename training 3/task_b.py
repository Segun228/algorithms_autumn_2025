def main():
    from collections import deque
    n = int(input())
    graph = [[] for el in range(n + 1)]
    for j in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    if n == 2:
        print(1)
        return 0
    leaves = [i for i in range(1, n + 1) if len(graph[i]) == 1]


    dist = [-1] * (n + 1)
    visited_from = dict()
    queue = deque()


    for leaf in leaves:
        dist[leaf] = 0
        visited_from[leaf] = leaf
        queue.append(leaf)

    answer = float('inf')

    while queue:
        u = queue.popleft()
        for neighbor in graph[u]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[u] + 1
                visited_from[neighbor] = visited_from[u]
                queue.append(neighbor)
            else:
                if visited_from[neighbor] != visited_from[u]:
                    path_length = dist[u] + dist[neighbor] + 1
                    if path_length < answer:
                        answer = path_length
    print(answer)

if __name__ == "__main__":
    main()