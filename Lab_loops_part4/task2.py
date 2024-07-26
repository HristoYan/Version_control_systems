def main():
    start = int(input('Enter start: '))
    end = int(input('Enter end: '))
    for i in range(start, end):
        if i % 2 != 0:
            print(i)


main()
