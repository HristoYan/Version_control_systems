def main():
    str_input = input('Enter an expression like 1 + 1: ')
    str_list = str_input.split(' ')
    first_num = int(str_list[0])
    second_num = int(str_list[2])
    result = 0
    if str_list[1] == '+':
        result = first_num + second_num
    elif str_list[1] == '-':
        result = first_num - second_num
    elif str_list[1] == '*':
        result = first_num * second_num
    elif str_list[1] == '/':
        result = first_num / second_num

    print(f'The result is: {result}')


if __name__ == '__main__':
    main()
