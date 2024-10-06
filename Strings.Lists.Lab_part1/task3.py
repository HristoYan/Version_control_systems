def main():
    text = input('Enter text: ')
    symbol = input('Enter symbol: ')
    symbol_counter = 0

    for c in text:
        if c == symbol:
            symbol_counter += 1

    print(f'The symbol appears {symbol_counter} times in the text.')


if __name__ == '__main__':
    main()
