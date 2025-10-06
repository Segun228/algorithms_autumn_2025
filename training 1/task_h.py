from collections import defaultdict

def main():
    reps = defaultdict(list)
    result = []
    n, m = map(int, input().split())
    s = input()
    piece_length = n//m
    for i in range(m):
        piece = input()
        reps[piece].append(i+1)
    for i in range(m):
        current_piece = s[i*piece_length:(i+1)*piece_length]
        index_of_valid_index, valid_index = next(
            (ind, x) for ind, x in enumerate(reps[current_piece]) if x >= 0
        )
        result.append(valid_index)
        reps[current_piece][index_of_valid_index] = -1
    print(*result)
    return 0



if __name__ == "__main__":
    main()