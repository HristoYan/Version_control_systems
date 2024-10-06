def main():

    books = [{'author': 'hristo',
                'title': 'My Stuff',
                'genre': 'fantasy',
                'year of release': '2024',
                'publisher': 'self'}]
    while True:
        action = input('Choose action (add, delete, search, and edit), \'done\' to exit: ').lower()
        if action == 'done':
            break

        if action in ['add', 'delete', 'search', 'edit']:
            if action == 'add':
                author = input('Enter author\'s full name: ').lower()
                title = input('Enter title: ')
                genre = input('Enter genre: ')
                year = input('Enter year of release: ')
                publisher = input('Enter publisher: ')
                info = {'author': author,
                        'title': title,
                        'genre': genre,
                        'year of release': year,
                        'publisher': publisher}
                books.append(info)

            elif action == 'delete':
                author = input('Enter author\'s name: ').lower()
                for a in range(len(books)):
                    if books[a]['author'] == author:
                        print(f'Author {author} has been deleted.')
                        books.pop(a)

            elif action == 'search':
                author = input('Enter author\'s name: ').lower()
                found = False
                for a in books:
                    searched_name = a['author']
                    if searched_name == author:
                        found = True
                        print(a)
                if not found:
                    print(f'{author} name does not exist.')

            elif action == 'edit':
                name = input('Enter author\'s name: ').lower()
                found = False
                for a in books:
                    searched = a['author']
                    if searched in name:
                        found = True
                        author = input('Replace author\'s name: ')
                        title = input('Replace title: ')
                        publisher = input('Replace publisher: ')
                        a['author'] = author
                        a['title'] = title
                        a['publisher'] = publisher
                        print('Changes are made.')
                if not found:
                    print(f'Author {name} does not exist.')

        else:
            print('Invalid action')

    print(books)


if __name__ == '__main__':
    main()
