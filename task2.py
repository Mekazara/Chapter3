print("Введите слова через пробелы")
words = input("").split()
words.sort(key=len)
for word in words:
    print(word, end=' ')







