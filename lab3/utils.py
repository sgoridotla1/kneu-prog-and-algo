from collections.abc import Callable


def normalize_word(word: str) -> str:
    return ''.join(char for char in word if char.isalnum()).lower()

def to_normilized_list(text: str, normalization_function: Callable) -> list[str]:
    words = text.split()
    normalized_words = [normalization_function(word) for word in words]
    return normalized_words
