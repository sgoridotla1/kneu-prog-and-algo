"""Варіант 64. Завдання 2. Групи однакових ключів після сортування за остачею"""
from utils import format_list
from validations import read_int_in_range, read_int_list

type Indexed = list[tuple[int, int]]

def mod_key(x: int) -> int:
    return x % 4

def insertion_sort(items: Indexed) -> Indexed:
    result = list(items)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and mod_key(result[j][0]) < mod_key(current[0]):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def merge(left: Indexed, right: Indexed) -> Indexed:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if mod_key(left[i][0]) >= mod_key(right[j][0]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(items: Indexed) -> Indexed:
    if len(items) <= 1:
        return list(items)

    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))

def get_groups(items: Indexed) -> list[str]:
    groups: list[list[int]] = []
    for value, _ in items:
        key = mod_key(value)
        if groups and groups[-1][0] == key:
            groups[-1][1] += 1
        else:
            groups.append([key, 1])
    return [f"{key}:{count}" for key, count in groups]

def main():
    n = read_int_in_range("", 0, 100)
    numbers = read_int_list("", n, -10**9, 10**9)

    indexed: Indexed = [(x, i) for i, x in enumerate(numbers)]
    by_insertion = insertion_sort(indexed)
    by_merge = merge_sort(indexed)

    print(f"Вставки: {format_list([value for value, _ in by_insertion])}")
    print(f"Злиття: {format_list([value for value, _ in by_merge])}")
    print(f"Позиції: {format_list([index for _, index in by_merge])}")
    print(f"Групи: {format_list(get_groups(by_merge))}")


if __name__ == "__main__":
    main()
