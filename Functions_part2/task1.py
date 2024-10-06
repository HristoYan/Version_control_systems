def main(nums: list):
    product = 0
    for i in nums:
        product += i

    return product


my_str = input('Enter seria of numbers separated by a ",": ')
my_list_str = my_str.split(', ')
my_list = [int(i) for i in my_list_str]
print(my_list)
if __name__ == '__main__':
    print(main(my_list))
