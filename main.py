# ДЗ: Анализ текста
import re


def count_words(text):
    counter = 0
    for word in text.split():
        counter += 1
    return counter


def longest_word(text):
    max_word = ""
    for word in text.split():
        if len(word) > len(max_word):
            max_word = word
    return max_word


def count_vowels(text):
    counter = 0
    vowels = "аеёиоуыэюя"
    for word in text.strip(' '):
        for ch in vowels:
            if word == ch:
                counter += 1
    return counter


def count_repeats(text):
    word_dict = {}
    for word in text.split():
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict


def main():
    # text = str(input("Введите текст для анализа: ")).lower().strip()
    text_file = open('example.txt', 'r', encoding="utf-8")
    text = text_file.read().lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    print(f"\nКоличество слов в тексте: {count_words(text)}")
    print(f"\nСамое длинное слово в тексте: {longest_word(text)}")
    print(f"\nКоличество гласных в тексте: {count_vowels(text)}")
    print("\nПовторы слов в тексте: ")
    for key, value in count_repeats(text).items():
        print(f"{key} : {value}")


main()
