from random import randint


def main(lst: list, number: int):
    counter = 0
    for i in range(len(lst)):
        if number in lst:
            counter += 1
            lst.remove(number)
        else:
            return counter


my_list = [randint(-100, 100) for i in range(20)]
print(my_list)
num = int(input('Enter a number to remove: '))

if __name__ == '__main__':
    print(main(my_list, num))
