from math import inf
def main():
    s = input().strip()
    n = int(input())
    words = set()
    max_word_len = 0
    for k in range(n):
        current = input().strip()
        words.add(current)
        max_word_len = max(max_word_len, len(current))
    dp = [-inf] * (len(s)+1)
    dp[0] = 0

    for i in range(1, len(s)+1):
        for j in range(1, min(max_word_len, i)+1):
            if dp[i-j] != -inf and s[i-j:i] in words:
                dp[i] = i-j
                break
    result = []
    index = len(s)
    while index > 0:
        start = dp[index]
        result.append(s[start:index])
        index = start

    for el in reversed(result):
        print(el, end= ' ')

if __name__ == "__main__":
    main()