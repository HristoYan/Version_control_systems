"""Потребителят въвежда две числа (начална и крайна точка на обхвата). Анализирайте всички числа в
този диапазон. Отпечатайте следното:

Всички числа в диапазона;
Всички числа в обхвата в низходящ ред;
Всички числа, които са кратни на 7;
Колко числа са кратни на 5."""

def main():
    start_num = int(input("Start: "))
    end_num = int(input("End: "))

    all_num = ''
    all_num_revers = ''
    sevenths = ''
    counter = 0
    for i in range(start_num, end_num):
        all_num += str(i) + " "
        all_num_revers += str(end_num - i) + " "

        if i % 7 == 0:
            sevenths += str(i) + " "

        if i % 5 == 0:
            counter += 1

    print(f"All the numbers: {all_num}")
    print(f"All the numbers reversed: {all_num_revers}")
    print(f"All the numbers divisible by 7: {sevenths}")
    print(f"The count of numbers divisible by 5: {counter}")


if __name__ == '__main__':
    main()
