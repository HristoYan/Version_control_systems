"""Заплатата на продавач е 200 USD + процент от продажбите, както следва: до 500 USD - 3%,
 от 500 до 1000 USD - 5%, над 1000 USD - 8%. Потребителят въвежда продажбите за трима продавачи.
  Определете тяхната заплата, най-добрия продавач, дайте му или ѝ бонус от 200 USD, отпечатайте резултата.
"""

def main():
    first_seller = int(input("Enter the sells of the first seller: "))
    second_seller = int(input("Enter the sells of the second seller: "))
    third_seller = int(input("Enter the sells of the third seller: "))

    salary = 200
    
    first_salary = 0
    second_salary = 0
    third_salary = 0
    
    if first_seller <= 500:
        first_salary = salary + (first_seller * 0.03)
    elif 500 < first_seller <= 1000:
        first_salary = salary + (first_seller * 0.05)
    else:
        first_salary = salary + (first_seller * 0.08)

    if second_seller <= 500:
        second_salary = salary + (second_seller * 0.03)
    elif 500 < second_seller <= 1000:
        second_salary = salary + (second_seller * 0.05)
    else:
        second_salary = salary + (second_seller * 0.08)

    if third_seller <= 500:
        third_salary = salary + (third_seller * 0.03)
    elif 500 < third_salary <= 1000:
        third_salary = salary + (third_seller * 0.05)
    else:
        third_salary = salary + (third_seller * 0.08)

    if first_seller > second_seller and first_seller > third_seller:
        first_salary += 200
    elif second_seller > first_seller and second_seller > third_seller:
        second_salary += 200
    else:
        third_salary += 200

    print(f"First seller: {first_salary}\nSecond seller: {second_salary}\nThird seller: {third_salary}")


if __name__ == '__main__':
    main()
