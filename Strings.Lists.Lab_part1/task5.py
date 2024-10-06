def main():
    text = input('Enter text: ')
    word = input('Enter a word to replace: ')
    replacement = input('Enter a replacement: ')

    new_text = text.replace(word, replacement)
    print(new_text)


if __name__ == '__main__':
    main()
