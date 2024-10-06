from random import randint


def main():
    my_list = [randint(-100, 100) for i in range(21)]
    sum_my_list = sum(my_list)
    print(sum_my_list)
    result = []
    print(my_list)
    if sum_my_list > 0:
        frag = my_list[0:int(len(my_list) * 2 / 3)]
        sorted_frag = sorted(frag)
        left_over = (my_list[int(len(my_list) * 2 / 3):])[::-1]
        result = sorted_frag + left_over
        print(left_over)

    else:
        frag = my_list[0:int(len(my_list) * 1 / 3)]

        sorted_frag = sorted(frag)
        left_over = (my_list[int(len(my_list) * 1 / 3):])[::-1]
        result = sorted_frag + left_over

    print(result)


if __name__ == '__main__':
    main()
