"""Напишете програма, която по избор на потребителя повишава въведеното число до степента на числата от 0 до 7."""


def main():
    number = int(input("Enter number: "))
    power = int(input("Choose a number between 0 nad 7, to see the power of the number you entered: "))

    print(f"the power of {number} on {power} is: {number ** power}")


if __name__ == '__main__':
    main()
