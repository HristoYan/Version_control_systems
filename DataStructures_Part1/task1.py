def main():
    user_input = input('Type a series of numbers separated by comma(, ): ')
    user_list = user_input.split(', ')
    print(user_input)
    print(user_list[::-1])
    while True:
        print('What would you like to do now: add, delete, display, check or replace("done" for exit): ')
        choice = input()
        if choice == 'add':
            new_input = input('Number ot add: ')
            if new_input not in user_list:
                user_list.append(new_input)
            else:
                print('The number is already in the list.')
        elif choice == 'delete':
            number_to_delete = input('Number to delete: ')
            new_list = []
            for n in user_list:
                if number_to_delete != n:
                    new_list.append(n)

            user_list = new_list[:]

        elif choice == 'display':
            start = input('You want to see the list from the start or from the end: ')
            if start == 'start':
                print(user_list)
            elif start == 'end':
                print(user_list[::-1])
            else:
                print('Invalid input!')
        elif choice == 'check':
            value = input('Value to check: ')
            if value in user_list:
                print('True')
            else:
                print('False')
        elif choice == 'replace':
            value = input('Number to replace: ')
            new_value = input('Number to replace it with: ')
            repetitions = input('One or all: ')
            temp_list = []
            if repetitions == 'All' or repetitions == 'all':
                for n in user_list:
                    if value == n:
                        temp_list.append(new_value)
                    else:
                        temp_list.append(n)

            elif repetitions == 'One' or repetitions == 'one':
                index = user_list.index(value)
                temp_list1 = user_list[:index]
                temp_list1.append(new_value)
                temp_list2 = user_list[index + 1:]
                temp_list = temp_list1 + temp_list2

            user_list = temp_list[:]
        elif choice == 'done':
            return
        else:
            print('invalid input! You can only choose between: add, delete, display, check or replace')
            continue


if __name__ == '__main__':
    main()
