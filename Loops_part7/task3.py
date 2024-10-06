
def main():
    start_num = int(input("Enter start number: "))
    end_num = int(input("Enter end number: "))

    for i in range(start_num, end_num + 1):
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")


if __name__ == '__main__':
    main()
