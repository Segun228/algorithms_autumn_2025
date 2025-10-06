def final_number(n: int, k: int) -> int:
    if n == 0 or k == 0:
        return n


    cycles = {
        1: (9, 45), 2: (4, 20), 3: (6, 29), 4: (7, 38),
        5: (1, 5), 6: (5, 26), 7: (8, 45), 8: (6, 34), 9: (3, 24),
    }

    while k > 0 and n % 10 != 0:
        last_digit = n % 10
        if last_digit == 0:
            break
        if last_digit in cycles and k >= cycles[last_digit][0]:
            cnt, s = cycles[last_digit]
            q = k // cnt
            n += q * s
            k -= q * cnt
        else:
            n += last_digit
            k -= 1

    return n

def main():
    n, k = map(int, input().split())
    print(final_number(n, k))
    return 0

if __name__ == "__main__":
    main()