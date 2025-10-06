def check_valid(
    row:int,
    col:int,
    matrix,
    el:str,
    h_checked:set,
    v_checked:set,
    main_diag_checked:set,
    sub_diag_checked:set
) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    h_count = 1
    v_count = 1
    main_diag_count = 1
    sub_diag_count = 1
    h_checked.add((row, col))
    v_checked.add((row, col))
    main_diag_checked.add((row, col))
    sub_diag_checked.add((row, col))
    dirs = ((1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
    for dir in dirs:
        x_dir, y_dir = dir
        current_position = [row, col]
        while (
            current_position[0]+x_dir>=0 and 
            current_position[0]+x_dir<n and 
            current_position[1]+y_dir>=0 and 
            current_position[1]+y_dir<m and 
            matrix[current_position[0] + x_dir][current_position[1] + y_dir] == el
        ):
            if abs(x_dir) == 1 and y_dir == 0:
                if (current_position[0] + x_dir, current_position[1] + y_dir) in h_checked:
                    break
                h_count += 1
                h_checked.add((current_position[0] + x_dir, current_position[1] + y_dir))
            elif abs(y_dir) == 1 and x_dir == 0:
                if (current_position[0] + x_dir, current_position[1] + y_dir) in v_checked:
                    break
                v_count += 1
                v_checked.add((current_position[0] + x_dir, current_position[1] + y_dir))
            elif (x_dir==1 and y_dir==1) or (x_dir==-1 and y_dir==-1):
                if (current_position[0] + x_dir, current_position[1] + y_dir) in main_diag_checked:
                    break
                main_diag_count += 1
                main_diag_checked.add((current_position[0] + x_dir, current_position[1] + y_dir))
            else:
                if (current_position[0] + x_dir, current_position[1] + y_dir) in sub_diag_checked:
                    break
                sub_diag_count += 1
                sub_diag_checked.add((current_position[0] + x_dir, current_position[1] + y_dir))
            current_position[0]+=x_dir
            current_position[1]+=y_dir
    if h_count >= 5 or v_count >= 5 or main_diag_count >= 5 or sub_diag_count >= 5:
        return True
    return False

def main():
    n, m = map(int, input().split())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = list(input().strip())
    h_checked = set()
    v_checked = set()
    main_diag_checked = set()
    sub_diag_checked = set()
    for row_ind, row in enumerate(matrix):
        for el_ind, el in enumerate(row):
            if el != '.' and check_valid(
                row = row_ind,
                col = el_ind,
                matrix = matrix,
                el = el,
                h_checked = h_checked,
                v_checked = v_checked,
                main_diag_checked = main_diag_checked,
                sub_diag_checked = sub_diag_checked
            ):
                print("Yes")
                return 0
    print("No")
    return 0


if __name__ == "__main__":
    main()