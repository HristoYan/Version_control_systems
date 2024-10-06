"""Ако числото е кратно на 3 (дели се на 3 без остатък), изведете думата Fizz. Ако то е кратно на 5, отпечатайте
Buzz. Ако то е кратно на 3 и 5, изведете Fizz Buzz. Ако числото не е кратно на 3 или 5, отпечатайте самото число."""


def main():
    start_num = int(input("Start: "))
    end_num = int(input("End: "))

    for i in range(start_num, end_num):

        if i % 3 == 0:
            print("Fizz ", end="")
            if i % 5 == 0:
                print("Buzz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(str(i) + " ", end="")


if __name__ == '__main__':
    main()
