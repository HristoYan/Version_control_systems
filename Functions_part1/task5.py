def main(start, end):

    if end < start:
        start, end = end, start
    my_list = [i for i in range(start, end + 1)]

    product_my_list = 0

    for j in my_list:
        product_my_list += j

    return product_my_list


first = int(input('Enter a number: '))
second = int(input('Enter a number: '))


if __name__ == '__main__':
    print(main(first, second))
