"""Потребителят въвежда число от 1 до 100. Ако числото е кратно на 3 (делимо на 3 без остатък), изведете думата
 Fizz. Ако числото е кратно на 5, изведете думата Buzz. Ако думата е кратна на 3 и 5, се извежда Fizz Buzz.
  Ако думата не е кратна на 3 и 5, отпечатайте числото.
Ако потребителят е въвел число извън обхвата, изведете съобщение за грешка."""


def main():

    number = int(input("Enter number between 1 nad 100: "))

    if 0 < number < 101:

        if number % 3 == 0:
            print("Fizz ", end="")

        if number % 5 == 0:
            print("Buzz")

        if number % 3 != 0 and number % 5 != 0:
            print(number)
    else:
        print("The number you've entered is not correct")
        return


if __name__ == '__main__':
    main()
