
def main():
    fr_en_dict = {'hi': 'bonjour', 'car': 'voiture', 'father': 'pere', 'mather': 'mere', 'man': 'homme', 'woman': 'famme'}
    while True:
        action = input('Choose action (add, delete, search, and replace), \'done\' to exit: ').lower()

        if action == 'done':
            break

        if action in ['add', 'delete', 'search', 'replace']:
            word = input('Enter word: ')

            if action == 'add':
                translation = input('Enter french meaning: ')
                if translation not in fr_en_dict:
                    fr_en_dict[word] = translation
                else:
                    print('Word already exist.')
            elif action == 'delete':
                print(f'Word {word} deleted.')
                del fr_en_dict[word]
            elif action == 'search':
                if word not in fr_en_dict:
                    print(f'Word {word} don\'t exist')
                else:
                    print(f'{word}: {fr_en_dict[word]}')
            elif action == 'replace':
                if word in fr_en_dict:
                    translation = input('Enter french meaning: ')
                    fr_en_dict[word] = translation
                else:
                    print(f'Word {word} dosn\'t exist.')
        else:
            print('Invalid action')

    print(fr_en_dict)


if __name__ == '__main__':
    main()
