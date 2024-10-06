"""Потребителят въвежда стойност на цяло число. Премахнете всички тройки и шестици от това цяло число и го отпечатайте."""


def main():
    number = input("Enter a number: ")
    result = ''
    for n in number:
        if n != '3' and n != '6':
            result += n

    print(f"The number striped from 3 and 6 is: {result}")


if __name__ == '__main__':
    main()
