"""Пребройте броя на целите числа в интервала от 100 до 999, които имат две еднакви цифри."""


def main():
    counter = 0
    for i in range(100, 1000):
        num = str(i)
        if num[0] == num[1]:
            counter += 1
        elif num[0] == num[2]:
            counter += 1
        elif num[1] == num[2]:
            counter += 1
    print(counter)

if __name__ == '__main__':
    main()
