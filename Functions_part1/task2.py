def even_num(first, second):
    for i in range(first, second):
        if i % 2 == 0:
            print(i)


start = int(input('Enter first number: '))
end = int(input('Enter second number: '))
even_num(start, end)
