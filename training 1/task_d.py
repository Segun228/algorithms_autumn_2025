from collections import Counter


def main():
    n, k = list(map(int, input().split()))

    topics = list(map(int, input().split()))
    if n<k:
        print(*topics)
        return 0
    topics_count = Counter(topics)
    if len(topics_count.keys()) > k:
        print(*list(topics_count.keys())[:k])
        return 0
    elif len(topics_count.keys()) == k:
        print(*list(topics_count.keys()))
        return 0
    result = list(topics_count.keys())
    for key in topics_count.keys():
        topics_count[key]-=1

    for key, value in topics_count.items():
        result.extend([key for _ in range(value)])
        if len(result) > k:
            result = result[:k]
            print(*result)
            return 0
    print(*result)
    return 0


if __name__ == '__main__':
    main()