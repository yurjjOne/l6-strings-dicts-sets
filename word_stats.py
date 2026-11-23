"""Л6, ДЗ 2. Кількість слів, кількість різних слів і три найчастіші.

Автор: Михайлюк Юрій, група МІТ-1026г
"""

PUNCT = ",.:;!?\"«»()—–-…"


def clean_words(text):
    """Прибрати розділові знаки, перевести в нижній регістр і розбити на слова."""
    for mark in PUNCT:
        text = text.replace(mark, " ")
    return text.lower().split()


def word_freq(words):
    """Словник «слово -> скільки разів»."""
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def word_stats(text):
    """Повертає (кількість слів, кількість різних слів)."""
    words = clean_words(text)
    freq = word_freq(words)
    return len(words), len(freq)


if __name__ == "__main__":
    sentence = input("Введіть речення: ")
    total, distinct = word_stats(sentence)
    print("Слів:", total)
    print("Різних слів:", distinct)
