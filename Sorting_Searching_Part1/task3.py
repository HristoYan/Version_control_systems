from random import randint


def main():
    my_list = [randint(-100, 100) for i in range(20)]
    print(my_list)
    n = len(my_list)

    for i in range(n - 1):
        counter = 0
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                counter += 1
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

        if counter == 0:
            print(my_list)
            return


if __name__ == '__main__':
    main()
