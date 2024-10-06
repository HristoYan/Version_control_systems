
def main():
    start_num = int(input("Enter start point: "))
    end_num = int(input("Enter end point: "))
    even_sum = 0
    odd_sum = 0
    nine_num = 0
    for i in range(start_num, end_num):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

        if i % 9 == 0:
            nine_num += i

    print(f"Even sum: {even_sum}, Odd sum: {odd_sum}, Divisible by nine sum: {nine_num}")


if __name__ == '__main__':
    main()
