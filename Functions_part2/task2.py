from random import randint


def main(lst: list):
    print(lst)
    return min(lst)


my_list = [randint(-100, 100) for i in range(20)]
if __name__ == '__main__':
    print(f'The minimum value is: {main(my_list)}')
