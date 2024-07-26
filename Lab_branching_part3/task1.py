def main():
    while True:
        number = input('Enter a six digit number and see if it is lucky or not: ')
        if len(number) == 6:
            first = number[:3]
            second = number[3:]
            first_result = 0
            second_result = 0
            for i in range(3):
                first_result += int(first[i])
                second_result += int(second[i])

            if first_result == second_result:
                print(f'Your number {number} is lucky')
            else:
                print(f'Your number {number} is wort nothing. Forget about it!')
            break
        else:
            print('I said six digits!')


if __name__ == '__main__':
    main()