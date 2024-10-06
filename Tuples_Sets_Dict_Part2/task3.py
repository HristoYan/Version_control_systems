def main():
    company = [{'full name': 'john smith',
                'phone number': '555-555-5555',
                'corporate email': 'john_smith@company.com',
                'job title': 'worker',
                'room number': '12',
                'skype': '@johnyskype'}]
    while True:
        action = input('Choose action (add, delete, search, and replace), \'done\' to exit: ').lower()
        if action == 'done':
            break

        if action in ['add', 'delete', 'search', 'replace']:
            if action == 'add':
                name = input('Enter full name: ').lower()
                number = input('Enter phone number: ')
                email = input('Enter email: ')
                job = input('Enter job title: ')
                room = input('Enter room number: ')
                skype = input('Enter person\'s skype: ')
                info = {'full name': name,
                        'phone number': number,
                        'corporate email': email,
                        'job title': job,
                        'room number': room,
                        'skype': skype}
                company.append(info)

            elif action == 'delete':
                name = input('Enter full name: ').lower()
                for n in range(len(company)):
                    if company[n]['full name'] == name:
                        print(f'Worker {name} has been deleted.')
                        company.pop(n)

            elif action == 'search':
                name = input('Enter full name: ').lower()
                found = False
                for n in company:
                    searched_name = n['full name']
                    if searched_name == name:
                        found = True
                        print(n)
                if not found:
                    print(f'{name} name does not exist.')

            elif action == 'replace':
                name = input('Enter full name: ').lower()
                found = False
                for n in company:
                    searched = n['full name']
                    if searched in name:
                        found = True
                        name = input('Replace full name: ')
                        job = input('Replace job title: ')
                        room = input('Replace room number: ')
                        n['full name'] = name
                        n['job title'] = job
                        n['room number'] = room
                        print('Changes are made.')
                if not found:
                    print(f'{name} does not exist.')

        else:
            print('Invalid action')

    print(company)


if __name__ == '__main__':
    main()
