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


def top_words(freq, k=3):
    """k найчастіших слів: спершу за частотою (спадання), при рівності — за абеткою."""
    pairs = sorted(freq.items(), key=lambda p: (-p[1], p[0]))
    return pairs[:k]


def word_stats(text):
    """Повертає (кількість слів, кількість різних слів, три найчастіші)."""
    words = clean_words(text)
    freq = word_freq(words)
    return len(words), len(freq), top_words(freq, 3)


if __name__ == "__main__":
    sentence = input("Введіть речення: ")
    total, distinct, top = word_stats(sentence)
    print("Слів:", total)
    print("Різних слів:", distinct)
    print("Три найчастіші:")
    for word, count in top:
        print(f"  {word} — {count}")
