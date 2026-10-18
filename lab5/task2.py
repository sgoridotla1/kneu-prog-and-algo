"""Варіант 64. Завдання 2. Стабільне сортування та відбір"""
from utils import Record, format_list, read_int, read_records, yes_no

def sort_key(record: Record) -> tuple[int, int]:
    _, _, value, count = record
    return value * count, value

def report_value(record: Record) -> int:
    _, _, value, count = record
    return value * count

def report_matches(record: Record, limit: int) -> bool:
    return report_value(record) <= limit

def insertion_sort(records: list[Record]) -> list[Record]:
    result = list(records)
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and sort_key(result[j]) > sort_key(current):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result

def merge(left: list[Record], right: list[Record]) -> list[Record]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if sort_key(left[i]) <= sort_key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def merge_sort(records: list[Record]) -> list[Record]:
    if len(records) <= 1:
        return list(records)

    mid = len(records) // 2
    return merge(merge_sort(records[:mid]), merge_sort(records[mid:]))

def is_ordered(result: list[Record]) -> bool:
    return all(
        sort_key(result[i - 1]) <= sort_key(result[i])
        for i in range(1, len(result))
    )

def has_same_records(original: list[Record], result: list[Record]) -> bool:
    return len(result) == len(original) and all(
        result.count(record) == original.count(record) for record in original
    )

def find_position(records: list[Record], code: int) -> int | None:
    for index, record in enumerate(records):
        if record[0] == code:
            return index
    return None

def is_stable(original: list[Record], result: list[Record]) -> bool:
    if len(result) != len(original):
        return False

    positions: list[int] = []
    for record in result:
        position = find_position(original, record[0])
        if (
            position is None
            or position in positions
            or sort_key(original[position]) != sort_key(record)
        ):
            return False
        positions.append(position)

    return all(
        positions[i] < positions[j]
        for i in range(len(result))
        for j in range(i + 1, len(result))
        if sort_key(result[i]) == sort_key(result[j])
    )

def check_report(original: list[Record], result: list[Record]) -> str:
    return (
        f"порядок {yes_no(is_ordered(result))}; "
        f"записи {yes_no(has_same_records(original, result))}; "
        f"стабільність {yes_no(is_stable(original, result))}"
    )

def codes(records: list[Record]) -> list[int]:
    return [record[0] for record in records]

def main():
    n = read_int()
    limit = read_int()
    records = read_records(n)
    snapshot = list(records)

    by_insertion = insertion_sort(records)
    unchanged = records == snapshot
    by_merge = merge_sort(records)
    unchanged = unchanged and records == snapshot

    print(f"Вставками: {format_list(codes(by_insertion))}")
    print(f"Злиттям: {format_list(codes(by_merge))}")
    print(f"Результати збігаються: {yes_no(by_insertion == by_merge)}")
    print(f"Вставки: {check_report(records, by_insertion)}")
    print(f"Злиття: {check_report(records, by_merge)}")
    print(f"Початкові дані збережено: {yes_no(unchanged)}")

    selected = [record for record in by_merge if report_matches(record, limit)]
    print(f"Записи з показником до {limit}:")
    if not selected:
        print("немає")
    for record in selected:
        print(f"{record[0]} | {record[1]} | {report_value(record)} грамів")
    print(f"Відібрано записів: {len(selected)}")
    print(f"Сума відібраних показників: {sum(report_value(record) for record in selected)}")


if __name__ == "__main__":
    main()
