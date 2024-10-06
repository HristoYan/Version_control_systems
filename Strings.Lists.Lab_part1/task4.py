def main():
    text = input('Enter text: ')
    text_list = text.split(' ')
    word = input('Enter word: ')
    word_counter = 0

    for w in text_list:
        if not w[-1].isalpha():
            temp = w[:-1]
            if temp == word:
                word_counter += 1
        if w == word:
            word_counter += 1

    print(f'The word appears {word_counter} times in the text.')


if __name__ == '__main__':
    main()
