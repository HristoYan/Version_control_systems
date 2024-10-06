def main():
    text = input('Enter some text: ')
    counter = 0
    for c in text:
        if c in ['.', '?', '!']:
            counter += 1

    print(f'There are {counter} sentences in your text')


if __name__ == '__main__':
    main()
