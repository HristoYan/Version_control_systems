def horizontal(symbol):
    for i in range(20):
        print(symbol, end='')


def vertical(symbol):
    for _ in range(20):
        print(symbol)


def line_display(symbol, func):
    func(symbol)


def main():
    symbol = input('Enter symbol to display: ')
    direction = input('Enter direction (\'h\' for horizontal and \'v\' for vertical: ')
    if direction == 'v':
        line_display(symbol, vertical)
    else:
        line_display(symbol, horizontal)


if __name__ == '__main__':
    main()
