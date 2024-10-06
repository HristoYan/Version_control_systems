
import sys


def main():
    result = 0
    max_num = -999999999
    min_num = 9999999999
    while True:
        num = int(input("Enter number, exit with 7: "))
        if num == 7:
            print("Good buy!")
            sys.exit()

        result += num
        if num > max_num:
            max_num = num

        if num < min_num:
            min_num = num

        print(f"The sum is: {result}, max number so far: {max_num}, min number so far: {min_num}")


if __name__ == '__main__':
    main()
