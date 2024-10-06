def main():
    string = input('Enter random numbers: ')
    string_list = string.split(' ' or ', ' or ',')
    nums_list = [int(i) for i in string_list]
    max_num = max(nums_list)
    min_num = min(nums_list)
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0

    for i in nums_list:
        if i > 0:
            positive_counter += 1
        elif i < 0:
            negative_counter += 1
        else:
            zero_counter += 1

    print(f'The largest: {max_num}\nThe smallest: {min_num}\nThe number of positive: {positive_counter}\n'
          f'The number of negative: {negative_counter}\nThe number of Zeros: {zero_counter}')


if __name__ == '__main__':
    main()
