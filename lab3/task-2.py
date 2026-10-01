"""Варіант 64. Завдання 2. Порівняння текстів: сумарна частота"""
from utils import normalize_word, to_normilized_list
from validations import (
    read_int_in_range,
    read_string_of_pattern,
)

text_pattern = r"^.{1,200}$"

def filter_by_length(words: list[str], min_len: int) -> list[str]:
    return [word for word in words if len(word) >= min_len]

def get_unique_words(words: list[str], common_words: list[str]) -> list[str]:
    unique = []
    for word in words:
        if word not in common_words and word not in unique:
            unique.append(word)
    return unique

def main():
    min_len = read_int_in_range("", 1, 20)
    min_total = read_int_in_range("", 1, 20)
    text_1 = read_string_of_pattern("", text_pattern)
    text_2 = read_string_of_pattern("", text_pattern)

    words_1 = filter_by_length(to_normilized_list(text_1, normalize_word), min_len)
    words_2 = filter_by_length(to_normilized_list(text_2, normalize_word), min_len)

    common_words = []
    for word in words_1:
        if word in words_2 and word not in common_words:
            common_words.append(word)

    print(f"Спільних слів: {len(common_words)}")

    selected_common_frequency = {}
    for word in common_words:
        freq = (words_1.count(word), words_2.count(word))
        if sum(freq) >= min_total:
            selected_common_frequency[word] = freq

    # print(common_words_frequency)
    print(f"Відібраних спільних: {len(selected_common_frequency)}")

    print("Відібрані слова і частоти:")

    if not selected_common_frequency:
        print("немає")

    for word, freq in selected_common_frequency.items():
        print(f"{word}: {" | ".join(map(str, freq))}")

    unique_1 = get_unique_words(words_1, common_words)
    unique_2 = get_unique_words(words_2, common_words)

    print(f"Лише в першому: {", ".join(unique_1) if unique_1 else 'немає'}")
    print(f"Лише в другому: {", ".join(unique_2) if unique_2 else 'немає'}")

    selected_common_total_count = sum(sum(freq) for freq in selected_common_frequency.values())
    print(f"Разом входжень відібраних: {selected_common_total_count}")

    selected_comprehension = [
        word for word in common_words
        if words_1.count(word) + words_2.count(word) >= min_total
    ]

    selected_generator = (
        word for word in common_words
        if words_1.count(word) + words_2.count(word) >= min_total
    )

    selected_loop = list(selected_common_frequency)

    print(
        "Цикл і включення:",
        "так" if selected_loop == selected_comprehension else "ні"
    )

    print(
        "Цикл і генератор:",
        "так" if selected_loop == list(selected_generator) else "ні"
    )

if __name__ == "__main__":
    main()
