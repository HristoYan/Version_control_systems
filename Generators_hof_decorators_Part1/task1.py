from random import randint


def main(x, y):
    if x > y:
        x, y = y, x

    my_list = [i for i in range(x, y)]
    print(my_list)
    odd_list = []
    for n in my_list:
        if n % 2 != 0:
            odd_list.append(n)

    return odd_list


n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
if __name__ == '__main__':
    print(main(n1, n2))
