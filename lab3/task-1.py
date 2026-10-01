import re

from validations import (
    cyrillic_pattern,
    punctuation_pattern,
    read_int_in_range,
    read_string_of_pattern,
)


def normalize_word(word):
    return ''.join(char for char in word if char.isalnum()).lower()

def get_match_by_pattern(string, pattern):
    nomalized_words = [normalize_word(word) for word in string.split()]

    words = [];
    for word in nomalized_words:
        if re.match(pattern, word):
            words.append(word)


    return words

def count_words(strings, pattern):
    matches = []

    # [
    #  [tovar, tovar]
    #  [tovar]
    #  [tovar]
    # ]
    for i, s in enumerate(strings):
        words = get_match_by_pattern(s, pattern)
        matches.append(words)

    total_matches = sum(len(words) for words in matches)
    unique_matches = len({word for words in matches for word in words})

    return matches, total_matches, unique_matches

def get_frequency(matches):
    frequency = {}

    if not matches:
        return None

    for line in matches:
        for word in line:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

def get_top_frequency(frequency, top_n=1):
    if not frequency:
        return None

    return frequency[:top_n]

def get_first_occurrence(matches, term):
    for i, words in enumerate(matches):
        if term in words:
            return i
    return None

def main():
    n = read_int_in_range("", 0, 30)
    letter = read_string_of_pattern("", rf"^[{cyrillic_pattern}]{{1}}$")
    term = read_string_of_pattern("", rf"^[{cyrillic_pattern}]{{1,20}}$")
    strings = []

    for i in range(n):
        s = read_string_of_pattern("", rf"^[{cyrillic_pattern}{punctuation_pattern}]{{1,200}}$")
        strings.append(s)


    letter_pattern = rf"^\w+{normalize_word(letter)}$"
    matches, total_matches, unique_matches = count_words(strings, letter_pattern)
    for i, words in enumerate(matches):
        print(f"Рядок {i + 1}: слів {len(words)}; різних {len(set(words))}")

    print(f"Усього слів: {total_matches}")
    print(f"Різних слів: {unique_matches}")

    print("Частоти:")
    frequency = get_frequency(matches)
    if not frequency:
        print("немає")
    else:
        for word, count in frequency:
            print(f"{word}: {count}")


    top_frequency = get_top_frequency(frequency)
    if not top_frequency:
        print("Найчастіше: немає")
    else:
        print(f"Найчастіше: {top_frequency[0][0]} ({top_frequency[0][1]})")


    term_pattern = rf"^{normalize_word(term)}$"
    term_matches, total_term_matches, _ = count_words(strings, term_pattern)

    first_occurace = get_first_occurrence(term_matches, normalize_word(term))
    first_seen = first_occurace + 1 if first_occurace is not None else "немає"

    print(f"Запит: {normalize_word(term)}; входжень: {total_term_matches}; перший рядок: {first_seen}")


if __name__ == "__main__":
    main()
