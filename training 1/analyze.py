
def main():
    counter = 0
    number = 19
    searching_for = number%10
    counter += 1
    total_sum = number%10
    number += number%10
    while number%10 != 2:
        counter += 1
        total_sum += number%10
        number += number%10
    print(f"Counter = {counter}")
    print(f"Total Sum = {total_sum}")



if __name__ == "__main__":
    main()

'''
2
Counter = 4
Total Sum = 20
final = 2

3
Counter = 6
Total Sum = 29
final = 2

4
Counter = 7
Total Sum = 38
final = 2

5
Counter = 1
Total Sum = 5
final = 0

6
Counter = 5
Total Sum = 26
final = 2

7
Counter = 8
Total Sum = 45
final = 2

8
Counter = 6
Total Sum = 34
final = 2

9
Counter = 3
Total Sum = 43
final = 2
'''