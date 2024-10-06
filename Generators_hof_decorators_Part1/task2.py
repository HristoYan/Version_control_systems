from random import randint


def main(lst: list, x: int, y: int):
    if x > y:
        x, y = y, x

    new_list = []
    for n in lst:
        if x > n or n > y:
            new_list.append(n)

    return new_list


my_list = [randint(0, 100) for _ in range(20)]
print(my_list)
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))

if __name__ == '__main__':
    print(main(my_list, n1, n2))
