# v1
# def main(positive_list: list):
#     result = 0
#     are_positive = True
#     for n in positive_list:
#         try:
#             if n < 0:
#                 raise ValueError
#             result += n
#         except ValueError:
#             print('Not all numbers in your list are positive!')
#             are_positive = False
#             break
#     if are_positive:
#         return result
#
#
# my_str = input('Enter positive numbers separated by comma (, ): ')
# my_str_list = my_str.split(', ')
# my_list = []
# for i in my_str_list:
#     my_list.append(int(i))
# if __name__ == '__main__':
#     print(main(my_list))


# v2
def main(positive_list: list):
    result = 0
    for i in positive_list:
        result += i
    return result


my_str = input('Enter positive numbers separated by comma (, ): ')
my_str_list = my_str.split(', ')
my_list = []
for i in my_str_list:
    my_list.append(int(i))
is_positive = True
for n in my_list:
    try:
        if n < 0:
            raise ValueError
    except ValueError:
        print('Not all numbers in your list are positive!')
        is_positive = False
        break


if __name__ == '__main__' and is_positive:
    print(main(my_list))
