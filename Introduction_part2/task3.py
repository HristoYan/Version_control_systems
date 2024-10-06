"""Напишете програма, която изчислява площта на диамант. Потребителят въвежда дължината на двата му диагонала."""


def main():
    first_diagonal = float(input("Enter first diagonal: "))
    second_diagonal = float(input("Enter second diagonal: "))

    area = (first_diagonal * second_diagonal) / 2

    print(f"The area of the diamond is {area}")


main()