# v1
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
#
# def main():
#     try:
#         number = int(input('Enter a positive number: '))
#         if number < 0:
#             raise ValueError
#         else:
#             print(factorial(number))
#     except ValueError:
#         print('The number must be positive')
#
#
# if __name__ == '__main__':
#     main()


# v2
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


try:
    number = int(input('Enter a positive number: '))
    if number < 0:
        raise ValueError
    else:
        print(factorial(number))
except ValueError:
    print('The number must be positive')


