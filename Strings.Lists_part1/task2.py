def main():
    text = input('Enter text: ')
    reserved_words = input('Enter reserved words: ')
    reserved_words_list = reserved_words.split(' ' or ', ' or ',')
    new_text = ''

    for w in reserved_words_list:
        if w in text:
            new_text = text.replace(w, w.upper())
            text = new_text

    print(new_text)


if __name__ == '__main__':
    main()
