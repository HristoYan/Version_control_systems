# You have three tuples of integers. Find elements present in all tuples.

import random


def main():
    list1 = [random.randint(0, 100) for i in range(20)]
    list2 = [random.randint(0, 100) for i in range(20)]
    list3 = [random.randint(0, 100) for i in range(20)]
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    tuple3 = tuple(list3)
    result = []

    for i in tuple1:
        if i in tuple2 and i in tuple3 and i not in result:
            result.append(i)

    # for i in range(len(tuple1)):
    #     for j in range(len(tuple2)):
    #         if tuple1[i] == tuple2[j]:
    #             for k in range(len(tuple3)):
    #                 if tuple1[i] == tuple3[k] and tuple1[i] not in result:
    #                     result.append(tuple1[i])

    print(result)


if __name__ == '__main__':
    main()
