"""Пребройте броя на целите числа в интервала от 100 до 9999, които имат различни цифри."""


def main():
    counter = 0
    for i in range(100, 10000):
        num = str(i)
        if len(num) == 3:
            if num[0] != num[1] and num[0] != num[2]:

                if num[1] != num[2]:
                    counter += 1

        else:
            if num[0] != num[1] and num[0] != num[2] and num[0] != num[3]:

                if num[1] != num[2] and num[1] != num[3]:

                    if num[2] != num[3]:
                        counter += 1
    print(counter)


if __name__ == '__main__':
    main()
