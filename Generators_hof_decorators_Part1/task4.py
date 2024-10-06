import timeit


def simple_decorator(func):
    exec_time = timeit.timeit(func, number=1)
    return exec_time


def even_num():
    my_list = [x for x in range(100000)]
    even_num_list = [num for num in my_list if num % 2 == 0]
    return even_num_list


print(even_num())
timed = simple_decorator(even_num)
print(f'{round(timed, 2)} sec')
