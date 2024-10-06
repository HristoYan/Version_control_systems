import random


def main():
    list1 = [random.randint(0, 100) for i in range(20)]
    list2 = [random.randint(0, 100) for i in range(20)]
    list3 = [random.randint(0, 100) for i in range(20)]
    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    tuple3 = tuple(list3)
    result1 = []
    result2 = []
    result3 = []

    for i in tuple1:
        if i not in tuple2 and i not in tuple3:
            result1.append(i)

    for i in tuple2:
        if i not in tuple1 and i not in tuple3:
            result2.append(i)

    for i in tuple3:
        if i not in tuple1 and i not in tuple2:
            result3.append(i)

    print(result1)
    print(result2)
    print(result3)


if __name__ == '__main__':
    main()
