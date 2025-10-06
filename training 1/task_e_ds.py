def main():
    n, k = map(int, input().split())
    if k == 0:
        print(n)
        return 0
    last_digit = n % 10
    if last_digit == 0:
        print(n)
        return
    elif last_digit == 5:
        print(n + 5)
        return 0
    current = n
    remaining_k = k
    while remaining_k > 0 and (current % 10) not in (2,4,6,8):
        current += current % 10
        remaining_k -= 1
    if remaining_k > 0:
        cycles = remaining_k // 4
        remainder_steps = remaining_k % 4
        current += cycles * 20
        for _ in range(remainder_steps):
            current += current % 10
    print(current)
    return 0

if __name__ == "__main__":
    main()