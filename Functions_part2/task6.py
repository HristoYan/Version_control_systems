from random import randint


def main(lst: list, power: int):
    powered_list = [i ** power for i in lst]

    return powered_list


my_list = [randint(0, 100) for i in range(10)]
print(my_list)
num = int(input('Enter a power number: '))
if __name__ == '__main__':
    print(main(my_list, num))