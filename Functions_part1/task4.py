def main(one, two, three, four, five):
    my_list = [one, two, three,four, five]
    min_number = min(my_list)
    return min_number


x = int(input('Enter number: '))
y = int(input('Enter number: '))
z = int(input('Enter number: '))
q = int(input('Enter number: '))
p = int(input('Enter number: '))


if __name__ == '__main__':
    print(main(x, y, z, q, p))