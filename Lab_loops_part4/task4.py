def main():
    start = int(input('Enter start: '))
    end = int(input('Enter end: '))
    my_list = []
    for i in range(start, end):
        my_list.append(i)

    my_list.reverse()
    for i in my_list:
        print(i)


main()
