"""Варіант 64. Завдання 1. Пошук до верхньої межі за кількістю цифр"""
from utils import format_list
from validations import read_int_in_range, read_int_list

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

def linear_search(numbers: list[int], t: int) -> list[int]:
    positions = []
    for i, x in enumerate(numbers):
        if digits_count(x) <= t:
            positions.append(i)
    return positions

def upper_bound(keyed: Indexed, t: int) -> int:
    """індекс першого елемента з ключем, більшим за t"""
    low, high = 0, len(keyed)
    while low < high:
        mid = (low + high) // 2
        if keyed[mid][0] <= t:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search(keyed: Indexed, t: int) -> list[int]:
    bound = upper_bound(keyed, t)
    return sorted(index for _, index in keyed[:bound])

def main():
    n = read_int_in_range("", 0, 100)
    numbers = read_int_list("", n, -10**9, 10**9)
    q = read_int_in_range("", 0, 100)
    queries = [read_int_in_range("", 0, 10**9) for _ in range(q)]

    keyed: Indexed = sorted(
        ((digits_count(x), i) for i, x in enumerate(numbers)),
        key=lambda pair: pair[0],
    )

    for t in queries:
        print(f"Лінійний: {format_list(linear_search(numbers, t))}")
        print(f"Бінарний: {format_list(binary_search(keyed, t))}")


if __name__ == "__main__":
    main()
