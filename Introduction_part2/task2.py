"""Потребителят въвежда три числа. Първото число е месечната заплата, второто число е размерът на месечната вноска по
заем, а третото е плащане за комунални услуги. Изведете на екрана сумата, с която потребителят ще разполага след
всички плащания."""


def main():
    salary = int(input("Enter salary: "))
    monthly_pay = int(input("Enter monthly payments: "))
    bills = int(input("Enter monthly bills: "))

    result = salary - monthly_pay - bills

    if result >= 0:
        print(f"You have {result}$ left.")
    else:
        print(f"Poor thing. You need {abs(result)}$ more")


main()
