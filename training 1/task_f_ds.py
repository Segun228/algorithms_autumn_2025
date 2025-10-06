from math import inf

def main():
    n, m = map(int, input().split())
    matrix = [input().strip() for _ in range(n)]
    row_sum = [0] * n
    row_unknown = [0] * n
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "+":
                row_sum[i] += 1
            elif matrix[i][j] == "-":
                row_sum[i] -= 1
            else:
                row_unknown[i] += 1
    col_sum = [0] * m
    col_unknown = [0] * m
    for j in range(m):
        for i in range(n):
            if matrix[i][j] == "+":
                col_sum[j] += 1
            elif matrix[i][j] == "-":
                col_sum[j] -= 1
            else:
                col_unknown[j] += 1
    result = -inf
    for i in range(n):
        for j in range(m):
            max_row = row_sum[i] + row_unknown[i]
            min_col = col_sum[j] - col_unknown[j]
            if matrix[i][j] == "?":
                max_row -= 1
                min_col += 1
            
            result = max(result, max_row - min_col)
    
    print(result)

if __name__ == "__main__":
    main()