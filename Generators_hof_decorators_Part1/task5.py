import timeit


def simple_decorator(func):
    def simple_wrapper():
        print(timeit.timeit(func, number=1))
    return simple_wrapper()


def even_num():
    x = int(input('Enter start: '))
    y = int(input('Enter end: '))
    my_list = [x for x in range(x, y)]
    even_num_list = [num for num in my_list if num % 2 == 0]
    print(even_num_list)
    return even_num_list


simple_decorator(even_num)
