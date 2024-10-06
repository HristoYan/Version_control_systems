def main():
    palindrome = input('Enter a text to check if it is a palindrome: ')
    palindrome = palindrome.lower()
    is_palindrome = True
    list_pal = palindrome.split(' ')
    as_one_word = ''.join(list_pal)
    length = len(as_one_word)

    if not (as_one_word[-1].isalpha()):
        as_one_word = as_one_word[0:length-1]
        length -= 1

    for i in range(0, int(length / 2)):
        if as_one_word[i] != as_one_word[(length - i - 1)]:
            is_palindrome = False
            break

    if is_palindrome:
        print('It is a Palindrome!')
    else:
        print('It is NOT a Palindrome!')


if __name__ == '__main__':
    main()
