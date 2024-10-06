# I did that it was interesting

class Dictionary:
    def __init__(self):
        self.dictionary = []

    def add_word(self, word, trans):
        self.dictionary.append({'word': word, 'translation': trans, 'popularity': 0})
        print(f'Word {word} successfully added!')

    def check_all(self):
        for dict_word in self.dictionary:
            print(f'Word: {dict_word['word']} - {dict_word['translation']}')

    def check_word(self, word):
        for dict_word in self.dictionary:
            if dict_word['word'] == word:
                dict_word['popularity'] += 1
                print(f'Word: {word} - {dict_word['translation']}')

    def replace_word(self, word, new_word):
        for dict_word in self.dictionary:
            if dict_word['word'] == word:
                dict_word['word'] = new_word

    def replace_translation(self, word, trans):
        for dict_word in self.dictionary:
            if dict_word['word'] == word:
                dict_word['translation'] = trans

    def delete_word(self, word):
        for dict_word in self.dictionary:
            if dict_word['word'] == word:
                self.dictionary.remove(dict_word)

    def least_popular(self):
        self.dictionary.sort(key=lambda x: x['popularity'])
        for i in range(10):
            print(f'Word {i}: {self.dictionary[i]}')

    def most_popular(self):
        self.dictionary.sort(reverse=True, key=lambda x: x['popularity'])
        for i in range(10):
            print(f'Word {i + 1}: {self.dictionary[i]}')


def dict_filling():
    ang_bg_dict = Dictionary()
    new_dict = [['hi', 'здравей'], ['buy', 'довиждане'], ['pen', 'химикал'], ['case', 'калъф'],
                ['chair', 'стол'], ['ear', 'ухо'], ['day', 'ден'], ['dog', 'куче'],
                ['glass', 'чаша'], ['water', 'вода'], ['remote control', 'дистанционно'],
                ['computer', 'компютър'],
                ['earring', 'обеца'], ['ring', 'пръстен'], ['book', 'книга'], ['dictionary', 'речник']]

    for word in new_dict:
        ang_bg_dict.add_word(word[0], word[1])
    while True:
        print('What would you like to do now?')
        choice = input('add, check, check all, replace word, replace translation, '
                       'delete, popular and least popular: ')
        if choice == 'add':
            word = input('Word: ')
            trans = input('Translation: ')
            ang_bg_dict.add_word(word, trans)

        elif choice == 'check':
            word = input('Word: ')
            ang_bg_dict.check_word(word)

        elif choice == 'check all':
            ang_bg_dict.check_all()

        elif choice == 'replace word':
            word = input('Word: ')
            new_word = input('Replacement: ')
            ang_bg_dict.replace_word(word, new_word)

        elif choice == 'replace translation':
            word = input('Word: ')
            new_trans = input('Replace translation with: ')
            ang_bg_dict.replace_translation(word, new_trans)

        elif choice == 'delete':
            word = input('Word: ')
            ang_bg_dict.delete_word(word)

        elif choice == 'popular':
            ang_bg_dict.most_popular()

        elif choice == 'least popular':
            ang_bg_dict.least_popular()

        else:
            break


dict_filling()
