import bisect

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    a = sorted(a)
    b = sorted(b)

    a_prefix = [0] * (len(a) + 1)
    b_prefix = [0] * (len(b) + 1)
    for i in range(len(a)):
        a_prefix[i + 1] = a_prefix[i] + a[i]
    for j in range(len(b)):
        b_prefix[j + 1] = b_prefix[j] + b[j]

    sum1 = 0 
    sum2 = 0
    for i in range(len(a)):
        current_el = a[i]
        el_ind = bisect.bisect_right(b, current_el)
        left_sum = current_el*el_ind  - b_prefix[el_ind]
        right_sum = (b_prefix[-1] - b_prefix[el_ind]) - (len(b) - el_ind) * current_el
        sum1 = sum1 + (i+1)*(left_sum+right_sum)
    for i in range(len(b)):
        current_el = b[i]
        el_ind = bisect.bisect_right(a, current_el)
        left_sum = current_el*el_ind  - a_prefix[el_ind]
        right_sum = (a_prefix[-1] - a_prefix[el_ind]) - (len(a) - el_ind) * current_el
        sum2 = sum2 + (i+1)*(left_sum+right_sum)
    print(sum1 - sum2)
    return 0
if __name__ == "__main__":
    main()