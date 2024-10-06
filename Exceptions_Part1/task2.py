# v1
# def main(name, age):
#     try:
#
#         if age < 0 or age > 130:
#             raise Exception
#         return f'Hello, {name}! Your age is {age}'
#     except Exception:
#         print('Age must be between 0 and 130')
#
#
# name = input('Enter name: ')
# age = int(input('Enter age: '))
# if __name__ == '__main__':
#     print(main(name, age))


# v2
def main(name, age):
    return f'Hello, {name}! Your age is {age}'


try:
    name = input('Enter name: ')
    age = int(input('Enter age: '))
    if age < 0 or age > 130:
        raise ValueError
    if __name__ == '__main__':
        print(main(name, age))
except ValueError:
    print('Age must be between 0 and 130')
