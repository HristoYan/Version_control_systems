def main(length: int, symbol: str, flag: str):
    for i in range(length):
        if flag == 'True':
            print(symbol * length)
        else:
            if i == 0 or i == length - 1:
                print(symbol * length)
            else:
                print(f'{symbol}{' ' * (length - 2)}{symbol}')


size = int(input('Enter size of the square: '))
sym = input('Enter symbol: ')
fl = input('Enter boolean: ')


if __name__ == '__main__':
    main(size, sym, fl)
