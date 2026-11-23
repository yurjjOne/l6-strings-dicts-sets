"""Тести до ДЗ Л6 (запуск: python3 test_l6.py)."""
from word_stats import word_stats, clean_words
from palindrome import is_palindrome

total, distinct, top = word_stats("To be, or not to be: that is the question. To be!")
assert total == 12 and distinct == 8
assert top == [("be", 3), ("to", 3), ("is", 1)]
assert word_stats("") == (0, 0, [])
assert word_stats("кіт кіт пес") == (3, 2, [("кіт", 2), ("пес", 1)])
assert clean_words("Привіт, світе!") == ["привіт", "світе"]

assert is_palindrome("А роза упала на лапу Азора")
assert is_palindrome("Я несу гусеня")
assert is_palindrome("Was it a car or a cat I saw?")
assert is_palindrome("12321")
assert not is_palindrome("Python")
assert is_palindrome("")

print("Усі тести пройдено")
