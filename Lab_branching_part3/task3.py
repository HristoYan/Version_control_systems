def main():
    month = int(input('Enter number of the month (1 - 12): '))
    if month in [1, 2, 12]:
        print('Winter is coming')
    elif month in [3, 4, 5]:
        print('Spring')
    elif month in [6, 7, 8]:
        print('Summer')
    elif month in [9, 10, 11]:
        print('Fall')
    else:
        print('Your number is not between 1 and 12')

main()