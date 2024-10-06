
def main():
    players = {}
    while True:
        name = input('Enter player\'s name or 7 for exit: ')

        if name == '7':
            break

        height = int(input('Enter player\'s height: '))
        players[name] = height

    action = input('Choose action (add, delete, search, and replace): ')
    if action in ['add', 'delete', 'search', 'replace']:
        new_name = input('Enter player\'s name: ')

        if action == 'add':
            height = int(input('Enter player\'s height: '))
            if new_name not in players:
                players[new_name] = height
            else:
                print('Player already exist.')
        elif action == 'delete':
            print(f'Player {new_name} deleted.')
            del players[new_name]
        elif action == 'search':
            print(f'Player: {new_name} height: {players[new_name]}')
        elif action == 'replace':
            if new_name in players:
                height = int(input('Enter player\'s height: '))
                players[new_name] = height
            else:
                print(f'Player {new_name} dosn\'t exist.')
    else:
        print('Invalid action')

    print(players)


if __name__ == '__main__':
    main()
