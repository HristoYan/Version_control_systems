"""Потребителят въвежда три числа. Намерете сумата и произведението на тези числа.
 Изведете резултата на екрана."""


def main():
    first_num = int(input("First number: "))
    second_num = int(input("Second number: "))
    third_num = int(input("Third number: "))

    sum_num = first_num + second_num + third_num
    product = first_num * second_num * third_num

    print(f"The sum is: {sum_num}, and the product is: {product}")


main()