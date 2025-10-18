def main():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    left = 0
    right = n
    min_k = -1
    while left <= right:
        k = (left + right) // 2
        flag = True
        carry = [a_i - b_i for a_i, b_i in zip(a, b)]
        places_left = [0] * n
        should_be_distributed = [0] * n
        for ind, car in enumerate(carry):
            if car < 0:
                places_left[ind] = -car
            else:
                should_be_distributed[ind] = car
        for i in range(n):
            if should_be_distributed[i] == 0:
                continue
            for j in range(max(0, i - k), min(n, i + k + 1)):
                if should_be_distributed[i] == 0:
                    break
                if places_left[j] > 0:
                    give = min(should_be_distributed[i], places_left[j])
                    should_be_distributed[i] -= give
                    places_left[j] -= give
            if should_be_distributed[i] > 0:
                flag = False
                break
        if flag:
            min_k = k
            right = k - 1
        else:
            left = k + 1
    print(min_k)
    return 0


if __name__ == "__main__":
    main()