class WordsFinder:

    file_names = []

    def __init__(self, *names):
        for name in names:
            self.file_names.append(name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(i, '')
                words = file.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_word[name] = words.index(word.lower()) + 1
        return find_word

    def count(self, word):
        count_word = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                count_word[name] = words.count(word.lower())
        return count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
