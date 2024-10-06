# bulls and cows
from random import randint


def get_magic_num():
    return randint(1000, 10000)


def get_hint(number, guess):
    num_str = str(number)
    guess_str = str(guess)
    counter_cows = 0
    counter_bulls = 0
    bulls_list = []
    for i in range(len(num_str)):
        if guess_str[i] in num_str:
            if guess_str[i] == num_str[i]:
                counter_cows += 1
                bulls_list.append(guess_str[i])

    for i in range(len(guess_str)):
        if guess_str[i] in num_str and guess_str[i] not in bulls_list:
            counter_bulls += 1

    print(f'You have a {counter_bulls} Bulls and {counter_cows} Cows.')


def main():
    magic_num = get_magic_num()
    print(magic_num)
    while True:
        guess = int(input('Enter your guess: '))
        if magic_num == guess:
            print('You won!')
            return
        else:
            get_hint(magic_num, guess)


if __name__ == '__main__':
    main()
