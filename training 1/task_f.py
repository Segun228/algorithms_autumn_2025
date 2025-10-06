from math import inf


def main():
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    if n==1 and m==1:
        print(0)
        return 0
        

    int_matrix = [[0 for _ in range(m)] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '+':
                int_matrix[i][j] = 1
            elif matrix[i][j] == '-':
                int_matrix[i][j] = -1
            else:
                int_matrix[i][j] = 0
    row_sum = []
    for row in int_matrix:
        current_sum = sum(row)
        zero_count = row.count(0)
        row_sum.append((current_sum, zero_count))
    col_sum = []
    for j in range(m):
        s = []
        for i in range(n):
            s.append(int_matrix[i][j])
        current_sum = sum(s)
        zero_count = s.count(0)
        col_sum.append((current_sum, zero_count))
    max_row_sum = -inf
    max_row_index = -1
    min_col_sum = inf
    min_col_index = -1
    for ind, item in enumerate(row_sum):
        if item[0] + item[1] > max_row_sum:
            max_row_sum = item[0] + item[1]
            max_row_index = ind
    for ind, item in enumerate(col_sum):
        if item[0] - item[1] < min_col_sum:
            min_col_sum = item[0] - item[1]
            min_col_index = ind
    if int_matrix[max_row_index][min_col_index] == 0:
        print(max_row_sum - min_col_sum - 2)
    else:
        print(max_row_sum - min_col_sum)
    return 0

if __name__ == "__main__":
    main()