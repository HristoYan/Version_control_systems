def main(num: str):
    is_palindrome = True
    for i in range(int(len(num) / 2)):

        if num[i] != num[len(num) - i - 1]:
            is_palindrome = False
            break

    return is_palindrome


number = input('Enter a number to check if it is a palindrome: ')
if __name__ == '__main__':
    print(main(number))
