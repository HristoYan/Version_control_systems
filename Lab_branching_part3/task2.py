def main():
    while True:
        number = input('Enter a six digit number and see if it is lucky or not: ')
        if len(number) == 6:
            first, second, third, fourth, fifth = number[5], number[4], number[2:4], number[1], number[0]
            print(first + second + third + fourth + fifth)
            break
        else:
            print('I said six digits!')


main()
