cyrillic_pattern = "А-Яа-яІіЇїЄєҐґ"
punctuation_pattern = r"!?,.\-:; "


def read_int_in_range(prompt: str, low: int, high: int):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue

        if low <= value <= high:
            return value
        print("Помилка: значення поза допустимим діапазоном.")

def read_string_of_pattern(prompt: str, pattern: str):
    import re
    while True:
        value = input(prompt)
        if re.match(pattern, value):
            return value
        print(f"Помилка: рядок не відповідає шаблону {pattern}.")
