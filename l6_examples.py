"""Л6, ДЗ 1. Приклади з лекції: спершу прогноз (коментар «прогноз»), потім запуск.

Архіву l6_files.zip у Classroom немає, тому дев'ять прикладів узято зі слайдів
і конспекту Л6 — по одному на кожну тему l6_01 … l6_09.
"""
import difflib
import unicodedata

print("--- 01. Індекси і зрізи")
s = "Hello, World"
print(len(s), s[0], s[-1], s[7:12], s[::-1])
# прогноз: 12 H d World dlroW ,olleH

print("--- 02. Коди символів")
print(ord("A"), ord("a"), chr(65), "A" < "a", ord("7") - ord("0"))
# прогноз: 65 97 A True 7

print("--- 03. Методи рядків")
print(repr(" hi ".strip()), "Hello".upper(), "a-b".replace("-", "+"),
      s.find("World"), "banana".count("a"), "-".join(["a", "b"]))
# прогноз: 'hi' HELLO a+b 7 3 a-b

print("--- 04. Порівняння рядків")
print("Hello" == "hello", "10" < "9", "Zebra" < "apple",
      " Так ".strip().lower() == "так")
# прогноз: False True True True

print("--- 05. Схожість і Unicode")
print(round(difflib.SequenceMatcher(None, "colour", "color").ratio(), 2),
      difflib.get_close_matches("pyton", ["python", "java", "ruby"]))
print("\u00e9" == "e\u0301", unicodedata.normalize("NFC", "e\u0301") == "\u00e9")
# прогноз: 0.91 ['python'] / False True

print("--- 06. Словник: операції")
prices = {"apple": 30, "milk": 45}
prices["bread"] = 25
prices["milk"] = 48
print(prices.get("tea"), prices.get("tea", 0), "milk" in prices, prices)
# прогноз: None 0 True {'apple': 30, 'milk': 48, 'bread': 25}

print("--- 07. Словник як лічильник")
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
# прогноз: {'b': 1, 'a': 3, 'n': 2}

print("--- 08. Множини")
a, b = {1, 2, 3, 4}, {3, 4, 5}
print(a | b, a & b, a - b, a ^ b, {1, 2} <= a, sorted(set([1, 2, 2, 3, 3])))
# прогноз: {1, 2, 3, 4, 5} {3, 4} {1, 2} {1, 2, 5} True [1, 2, 3]

print("--- 09. Частота слів")
text = "To be, or not to be: that is the question. To be!"
for mark in ",.:!":
    text = text.replace(mark, "")
freq = {}
for word in text.lower().split():
    freq[word] = freq.get(word, 0) + 1
print(freq, len(freq))
# прогноз: to 3, be 3, решта по 1; 8 різних слів
