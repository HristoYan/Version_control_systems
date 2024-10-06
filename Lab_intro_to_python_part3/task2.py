while True:
    number = input('Enter a three digit number: ')
    result = 0
    if len(number) == 3:
        for n in number:
            result += int(n)
            print(n)
        print(result)
        break
