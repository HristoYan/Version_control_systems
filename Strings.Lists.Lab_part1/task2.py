def main():
    text = input('Enter text: ')
    letters_counter = 0
    numbers_counter = 0

    for c in text:
        if c.isalpha():
            letters_counter += 1
        if c.isdigit():
            numbers_counter += 1

    print(f'You have: {letters_counter} letters and {numbers_counter} digits')


if __name__ == '__main__':
    main()
