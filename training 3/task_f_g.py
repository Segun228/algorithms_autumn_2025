import sys
input = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**5)
def main():
    n = int(input())
    parent_nodes = list(map(int, input().split()))
    tree = [[] for kkk in range(n)]
    timecount = [[-1, -1] for _ in range(n)]
    root_node = -1

    for ind, el in enumerate(parent_nodes):
        if el != 0:
            tree[el - 1].append(ind)
        else:
            root_node = ind

    counter = 0
    stack = [(root_node, 0)]
    enter = [False] * n

    while stack:
        node, child_idx = stack.pop()
        if not enter[node]:
            timecount[node][0] = counter
            counter += 1
            enter[node] = True
            stack.append((node, 0))
            if tree[node]:
                for child in reversed(tree[node]):
                    stack.append((child, 0))
        elif child_idx == 0:
            timecount[node][1] = counter
            counter += 1

    m = int(input())
    for j in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if (timecount[a][0] <= timecount[b][0]) and timecount[b][0] <= timecount[b][1] and (timecount[b][1] <= timecount[a][1]):
            write("1\n")
        else:
            write("0\n")
    return 0

if __name__ == "__main__":
    main()