
import random


def board_view(my_list: list, board: list):
    compare_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    compare_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    while True:
        if my_list == compare_list1 or my_list == compare_list2:
            print('You won!')
            break

        board[0] = my_list[0:4]
        board[1] = my_list[4:8]
        board[2] = my_list[8:12]
        board[3] = my_list[12:16]

        zero_index = my_list.index(0)
        print(zero_index)
        for line in board:
            print('------------------')
            for n in line:
                print(n, end=' | ')
            print()
        print('------------------')
        choice = int(input('Enter value for swapping: '))
        if choice <= 0 or choice > 15:
            print('Incorrect choice!')
            continue
        index_choice = my_list.index(choice)

        right_choice = [zero_index - 1, zero_index + 1, zero_index - 4, zero_index + 4]
        print(right_choice)
        if index_choice in right_choice:
            my_list[index_choice], my_list[zero_index] = my_list[zero_index], my_list[index_choice]
            board_view(my_list, board)
        else:
            print('Incorrect choice!')


def main():
    board = [[], [], [], []]
    my_list = []
    for i in range(16):
        my_list.append(i)

    random.shuffle(my_list)
    board_view(my_list, board)


if __name__ == '__main__':
    main()
