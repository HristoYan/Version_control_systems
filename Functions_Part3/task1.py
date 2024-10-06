def main(n1, n2):
    if n2 == 0:
        return n1
    else:
        return main(n2, n1 % n2)


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if __name__ == '__main__':
    print(f'The Greatest Common Divisor of {num1} and {num2} is: {main(num1, num2)}')
