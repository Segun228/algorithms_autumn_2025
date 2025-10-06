def check_valid(row: int, col: int, matrix, el: str, checked: list) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    
    for dir_idx, (dx, dy) in enumerate(directions):
        if checked[row][col][dir_idx]:
            continue
        
        count = 1
        checked[row][col][dir_idx] = True
        
        r, c = row + dx, col + dy
        while 0 <= r < n and 0 <= c < m and matrix[r][c] == el:
            count += 1
            checked[r][c][dir_idx] = True
            r += dx
            c += dy
        
        r, c = row - dx, col - dy
        while 0 <= r < n and 0 <= c < m and matrix[r][c] == el:
            count += 1
            checked[r][c][dir_idx] = True
            r -= dx
            c -= dy
        
        if count >= 5:
            return True
    return False

def main():
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = list(input().strip())
    checked_lines = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    for row_ind in range(n):
        for col_ind in range(m):
            el = matrix[row_ind][col_ind]
            if el == '.':
                continue

            has_neighbor = False
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    r, c = row_ind + dr, col_ind + dc
                    if 0 <= r < n and 0 <= c < m and matrix[r][c] == el:
                        has_neighbor = True
                        break
                if has_neighbor:
                    break

            if not has_neighbor:
                continue
            
            if check_valid(row_ind, col_ind, matrix, el, checked_lines):
                print("Yes")
                return
    print("No")

if __name__ == "__main__":
    main()