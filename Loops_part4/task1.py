"""Потребителят въвежда две числа (начална и крайна точка на обхвата). Анализирайте всички числа в този диапазон,
както следва: ако числото е кратно на 7, го отпечатайте."""


def main():
    start_num = int(input("Start: "))
    end_num = int(input("End: "))

    for i in range(start_num, end_num):
        if i % 7 == 0:
            print(i)


if __name__ == '__main__':
    main()
