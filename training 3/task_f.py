import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
write = sys.stdout.write

def dfs(node, tree, timecount, counter):
    timecount[node][0] = counter
    counter += 1
    for child in tree[node]:
        counter = dfs(child, tree, timecount, counter)
    timecount[node][1] = counter
    counter += 1
    return counter


def main():
    n = int(input())
    parent_nodes = list(map(int, input().split()))
    tree = [[] for i in range(n)]
    timecount = [[-1, -1] for i in range(n)]
    root_node = -1


    for ind, el in enumerate(parent_nodes):
        if el != 0:
            tree[el - 1].append(ind)
        else:
            root_node = ind

    dfs(root_node, tree, timecount, 0)
    m = int(input())
    for i in range(m):
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