"""Варіант 64. Завдання 1. Пошук до верхньої межі за кількістю цифр"""
from utils import format_list, read_int, read_int_list

type Indexed = list[tuple[int, int]]

def digits_count(x: int) -> int:
    x = abs(x)
    if x == 0:
        return 1

    count = 0
    while x > 0:
        x //= 10
        count += 1
    return count

def insertion_sort_by_key(items: Indexed) -> Indexed:
    """стабільне сортування пар (число, позиція) за зростанням кількості цифр"""
    result = list(items)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and digits_count(result[j][0]) > digits_count(current[0]):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def insertion_sort_positions(positions: list[int]) -> list[int]:
    result = list(positions)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def linear_search(indexed: Indexed, t: int) -> list[int]:
    positions = []
    for value, index in indexed:
        if digits_count(value) <= t:
            positions.append(index)
    return positions

def upper_bound(keyed: Indexed, t: int) -> int:
    """індекс першого елемента з ключем, більшим за t"""
    low, high = 0, len(keyed)
    while low < high:
        mid = (low + high) // 2
        if digits_count(keyed[mid][0]) <= t:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search(keyed: Indexed, t: int) -> list[int]:
    bound = upper_bound(keyed, t)
    return insertion_sort_positions([index for _, index in keyed[:bound]])

def main():
    n = read_int()
    numbers = read_int_list(n)
    q = read_int()
    queries = [read_int() for _ in range(q)]

    indexed: Indexed = [(x, i) for i, x in enumerate(numbers)]
    keyed = insertion_sort_by_key(indexed)

    for t in queries:
        print(f"Лінійний: {format_list(linear_search(indexed, t))}")
        print(f"Бінарний: {format_list(binary_search(keyed, t))}")


if __name__ == "__main__":
    main()
