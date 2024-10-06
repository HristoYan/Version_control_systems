def main(num):
    return len(num)


number = input('Enter a number: ')
if __name__ == '__main__':
    print(f'Your number has {main(number)} digits')
