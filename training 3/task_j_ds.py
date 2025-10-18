def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    if sum(a) > sum(b):
        print(-1)
        return 0

    left = 0
    right = n
    min_k = -1

    while left <= right:
        k = (left + right) // 2
        flag = True

        remaining_people = a.copy()
        p = 0

        for i in range(n):
            while p < n and remaining_people[p] == 0:
                p += 1
            if p < n and p < i - k:
                flag = False
                break
            cap = b[i]
            while cap > 0:
                while p < n and remaining_people[p] == 0:
                    p += 1
                if p >= n:
                    break
                if p > i + k:
                    break
                take = min(cap, remaining_people[p])
                remaining_people[p] -= take
                cap -= take
                if remaining_people[p] == 0:
                    p += 1
        if flag:
            while p < n and remaining_people[p] == 0:
                p += 1
            if p < n:
                flag = False
        if flag:
            min_k = k
            right = k - 1
        else:
            left = k + 1
    print(min_k)
    return 0


if __name__ == "__main__":
    main()