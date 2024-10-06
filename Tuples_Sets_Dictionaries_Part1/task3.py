# You have three tuples of integers. Find elements that are present in each tuple
# and at the same position in each tuple.

import random


def main():
    # list1 = [random.randint(0, 100) for i in range(20)]
    # list2 = [random.randint(0, 100) for i in range(20)]
    # list3 = [random.randint(0, 100) for i in range(20)]
    # tuple1 = tuple(list1)
    # tuple2 = tuple(list2)
    # tuple3 = tuple(list3)
    tuple1 = 1, 2, 3, 4, 6, 8
    tuple2 = 2, 1, 3, 4, 7, 8
    tuple3 = 1, 2, 3, 4, 6, 8
    result = []

    for i in tuple1:

        if i in tuple2 and i in tuple3:
            if tuple1.index(i) == tuple2.index(i) == tuple3.index(i):
                result.append(i)

    print(result)


if __name__ == '__main__':
    main()
