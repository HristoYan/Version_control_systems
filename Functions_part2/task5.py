from random import randint


def main(list1: list, list2: list):
    return list1 + list2


list_1 = [randint(-100, 100) for i in range(10)]
list_2 = [randint(-100, 100) for i in range(10)]
if __name__ == '__main__':
    print(main(list_1, list_2))
