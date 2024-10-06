
import sys

def main():
    while True:
        num = int(input("Enter number: "))
        if num == 7:
            print("Good buy!")
            sys.exit()
        elif num > 0:
            print("Your number is positive.")
        elif num < 0:
            print("Your number is negative")
        else:
            print("Your number is zero")


if __name__ == '__main__':
    main()
