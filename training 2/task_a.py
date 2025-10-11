
def main():
    n = int(input())
    stairs = [0] * (n+3)
    stairs[0] = 1
    for i in range(0, n):
        stairs[i+1] += stairs[i]
        stairs[i+2] += stairs[i]
        stairs[i+3] += stairs[i]
    print(stairs[n])

if __name__ == "__main__":
    main()