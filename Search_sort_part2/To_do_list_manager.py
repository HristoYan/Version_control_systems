import sys


def main():
    to_do_list = []
    print('To-Do List Manager:\n1. Add item\n2. Remove item\n3. View list\n4. Exit')
    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:
            to_do = input('Enter new to-do item: ')
            to_do_list.append(to_do)
        elif choice == 2:
            index = int(input('Enter index of item to remove: '))
            to_do_list.pop(index - 1)
        elif choice == 3:
            print('Current To-Do List:')
            for i, do in enumerate(to_do_list):
                print(f'{i + 1}. {do}')
        else:
            print('Goodbye!')
            sys.exit()


if __name__ == '__main__':
    main()
