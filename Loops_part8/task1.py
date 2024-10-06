def main():

#  condition a
    print('condition a')
    for i in range(0, 10):
        print("   " * i, end="")
        print("*  " * (10 - i))

     # condition b
    print('condition b')

    for i in range(0, 10):
        print("*  " * (i - 1))

    # condition c
    print('condition c')

    for i in range(0, 10):
        if i % 2 == 0:
            print('  ' * i, end='')
            print('*   ' * (12 - i - 2))

    for j in range(0, 5):
        print('   ' * 10)

    # condition d
    print('condition d')

    for i in range(0, 5):
        print(' ' * 10)

    for j in range(0, 12):

        if j % 2 == 0:
            print('  ' * (12 - j - 2), end='')
            print('*   ' * j)

    # condition e
    print('condition e')

    for i in range(0, 10):
        if i % 2 == 0:
            print('  ' * i, end='')
            print('*   ' * (12 - i - 2))

    for j in range(0, 12):
        if j % 2 == 0:
            print('  ' * (12 - j - 2), end='')
            print('*   ' * j)

    # condition f
    print('condition f')

    for i in range(1, 11):
        if i <= 5:
            print('*  ' * i, end='')
            print('   ' * (10 - (2 * i)), end='')
            print('*  ' * i)
        if i > 5:
            print('*  ' * (10 - i), end='')
            print('   ' * (2 * i - 10), end='')
            print('*  ' * (10 - i))

    # condition g
    print('condition g')

    for i in range(1, 11):
        if i <= 5:
            print('*  ' * i)

        if i > 5:
            print('*  ' * (10 - i))

    # condition h
    print('condition h')

    for i in range(1, 11):
        if i <= 5:

            print('   ' * (10 - i), end='')
            print('*  ' * i)
        if i > 5:
            print('   ' * i, end='')
            print('*  ' * (10 - i))
    #  condition i
    print('condition i')

    for i in range(10, 0, -1):
        print("*  " * (i - 1))

    #  condition j
    print('condition j')

    for i in range(0, 10):
        print("   " * (10 - i), end="")
        print("*  " * i)


if __name__ == '__main__':
    main()
