# # # v1
# def main():
#     my_str = input('Enter a list of numbers separated by comma (, ): ')
#     my_str_list = my_str.split(', ')
#     my_list = []
#     for n in my_str_list:
#         my_list.append(int(n))
#
#     print('If you want to display the list of numbers press 1')
#     print('If you want to display the maximum number press 2')
#     print('If you want to display the minimum number press 3')
#     print('If you want to display the value at given index press 4')
#     print('If you want to delete a value at given index press 5')
#     print('For Exit press 6')
#
#     while True:
#         choice = input('Enter your choice: ')
#         if choice == '1':
#             print(my_list)
#         elif choice == '2':
#             print(max(my_list))
#         elif choice == '3':
#             print(min(my_list))
#         elif choice == '4':
#             try:
#                 index = int(input('Enter index: '))
#                 if index < 0 or index > len(my_list) - 1:
#                     raise ValueError
#                 else:
#                     print(my_list[index])
#             except ValueError:
#                 print(f'Invalid input! Try an index between 0 and {len(my_list) - 1}')
#         elif choice == '5':
#             try:
#                 index = int(input('Enter index: '))
#                 if index < 0 or index > len(my_list) - 1:
#                     raise ValueError
#                 else:
#                     num = my_list.pop(index)
#                     print(f'The number {num} at index {index} has been removed.')
#             except ValueError:
#                 print(f'Invalid input! Try an index between 0 and {len(my_list) - 1}')
#         elif choice == '6':
#             break


# v2 it isn't exactly as the task, but I don't see how can we take the try-except block outside the function!
def display_index(lst: list):
    try:
        index = int(input('Enter index: '))
        if index < 0 or index > len(lst) - 1:
            raise ValueError
        else:
            print(lst[index])
    except ValueError:
        print(f'Invalid input! Try an index between 0 and {len(lst) - 1}')


def delete_index(lst: list):
    try:
        index = int(input('Enter index: '))
        if index < 0 or index > len(lst) - 1:
            raise ValueError
        else:
            num = lst.pop(index)
            print(f'The number {num} at index {index} has been removed.')
    except ValueError:
        print(f'Invalid input! Try an index between 0 and {len(lst) - 1}')


def main():
    my_str = input('Enter a list of numbers separated by comma (, ): ')
    my_str_list = my_str.split(', ')
    my_list = []
    for n in my_str_list:
        my_list.append(int(n))

    print('If you want to display the list of numbers press 1')
    print('If you want to display the maximum number press 2')
    print('If you want to display the minimum number press 3')
    print('If you want to display the value at given index press 4')
    print('If you want to delete a value at given index press 5')
    print('For Exit press 6')

    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            print(my_list)
        elif choice == '2':
            print(max(my_list))
        elif choice == '3':
            print(min(my_list))
        elif choice == '4':
            display_index(my_list)
        elif choice == '5':
            delete_index(my_list)
        elif choice == '6':
            break


if __name__ == '__main__':
    main()
