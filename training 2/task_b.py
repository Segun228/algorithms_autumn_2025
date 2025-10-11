def main():
    s = input()
    n = len(s)
    s = list(s)
    river = [[0] * (n+2) for _ in range(2)]
    river[1][0] = 1
    for ind, el in enumerate(s):
        if el == 'L':
            river[1][ind+1]= river[1][ind]
            river[0][ind+1] = min(river[0][ind] + 1, river[1][ind+1] + 1)
        elif el == 'R':
            river[0][ind+1]= river[0][ind]
            river[1][ind+1] = min(river[1][ind] + 1, river[0][ind+1] + 1)
        else:
            river[0][ind+1] = river[0][ind] + 1
            river[1][ind+1] = river[1][ind] + 1
    print(river[1][n])
    return 0



if __name__ == "__main__":
    main()