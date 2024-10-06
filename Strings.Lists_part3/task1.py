def main():
    first_list = [1, 2, 3, 4, 5, 6, 7, 8]
    second_list = [2, 4, 6, 8, 10, 12, 14, 16]
    third_list = first_list + second_list
    non_rep_elements_list = []
    rep_elements_list = []
    unique_elements_first_list = [i for i in first_list if i not in second_list]
    unique_elements_second_list = [j for j in second_list if j not in first_list]
    min_max_list = [min(third_list), max(third_list)]

    for el in third_list:
        if el not in non_rep_elements_list:
            non_rep_elements_list.append(el)
        if el in first_list and el in second_list and el not in rep_elements_list:
            rep_elements_list.append(el)

    print(f'All elements: {third_list}')
    print(f'Non repeating: {non_rep_elements_list}')
    print(f'Repeating: {rep_elements_list}')
    print(f'Unique for the first: {unique_elements_first_list}')
    print(f'Unique for the second: {unique_elements_second_list}')
    print(f'Min Max: {min_max_list}')


if __name__ == '__main__':
    main()
