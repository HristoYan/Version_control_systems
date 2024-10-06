def main():
    shopping_list = []
    while True:
        item_category = input('Enter item and category (or type "Done" to finish):\n')
        item_category_list = item_category.split(', ')

        if item_category_list[0] == 'Done':
            break

        item, category = item_category_list[0], item_category_list[1]
        shopping_list.append({item: category})

    category_list = []
    for cat in shopping_list:
        for v in cat.values():
            if v not in category_list:
                category_list.append(v)

    for c in category_list:
        print(f'Category: {c}')
        for i in shopping_list:
            for x, y in i.items():
                if c == y:
                    print(f'- {x}')
        print()


if __name__ == '__main__':
    main()
