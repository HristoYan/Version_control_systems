first_num = int(input("Enter a Number: "))
second_num = int(input("Enter a Number to compare: "))

if first_num == second_num:
    print(f"{first_num} and {second_num} are equal")
elif first_num > second_num:
    print(second_num, first_num)
else:
    print(first_num, second_num)
