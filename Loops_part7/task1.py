
def main():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))

    for i in range(first_num, second_num):
        if i % 2 != 0:
            print(i)


if __name__ == '__main__':
    main()
