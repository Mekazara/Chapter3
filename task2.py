print("Введите слова через пробелы")
words = input("")
list_of_words = list(words.split())
list_of_words.sort(key=len)
for word in list_of_words:
    print(word, end=' ')







