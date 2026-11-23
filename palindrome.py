"""Л6, ДЗ 3. Перевірка паліндрома без урахування регістру, пробілів і розділових знаків.

Автор: Михайлюк Юрій, група МІТ-1026г
"""


def normalize(text):
    """Лишити тільки літери й цифри в нижньому регістрі."""
    result = ""
    for ch in text.lower():
        if ch.isalnum():
            result += ch
    return result


def is_palindrome(text):
    """True, якщо текст читається однаково зліва направо і справа наліво."""
    s = normalize(text)
    return s == s[::-1]


if __name__ == "__main__":
    phrase = input("Введіть слово або фразу: ")
    if is_palindrome(phrase):
        print("Так, це паліндром")
    else:
        print("Ні, це не паліндром")
