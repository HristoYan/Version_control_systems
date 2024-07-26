def main():
    start = int(input('Enter start: '))
    end = int(input('Enter end: '))
    if start > end:
        start, end = end, start

    for i in range(start, end):
        if i % 2 != 0:
            print(i)


main()
