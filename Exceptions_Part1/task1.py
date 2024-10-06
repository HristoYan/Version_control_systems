def main():
    try:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        if age < 0 or age > 130:
            raise Exception
        print(f'Hello, {name}! Your age is {age}')
    except Exception:
        print('Age must be between 0 and 130')


if __name__ == '__main__':
    main()
