"""Варіант 64. Завдання 1. Перевірка записів і пошук за кодом"""
from utils import Record, format_list, read_int, read_records, yes_no

type Found = tuple[int | None, int]

MAX_CODE = 9999
MAX_VALUE = 50000
MAX_COUNT = 100

def is_valid(record: Record) -> bool:
    code, _, value, count = record
    return 1 <= code <= MAX_CODE and 0 <= value <= MAX_VALUE and 0 <= count <= MAX_COUNT

def has_code(records: list[Record], code: int) -> bool:
    return any(record[0] == code for record in records)

def validate_records(records: list[Record]) -> tuple[list[Record], list[str]]:
    accepted: list[Record] = []
    rejected: list[str] = []
    for number, record in enumerate(records, start=1):
        if not is_valid(record):
            rejected.append(f"Запис {number}: відхилено (недопустимі значення)")
        elif has_code(accepted, record[0]):
            rejected.append(f"Запис {number}: відхилено (повтор коду {record[0]})")
        else:
            accepted.append(record)
    return accepted, rejected

def linear_search(records: list[Record], code: int) -> Found:
    checked = 0
    for index, record in enumerate(records):
        checked += 1
        if record[0] == code:
            return index, checked
    return None, checked

def binary_search(records: list[Record], code: int) -> Found:
    checked = 0
    left, right = 0, len(records) - 1
    while left <= right:
        mid = (left + right) // 2
        checked += 1
        if records[mid][0] == code:
            return mid, checked
        if records[mid][0] < code:
            left = mid + 1
        else:
            right = mid - 1
    return None, checked

def pick(records: list[Record], index: int | None) -> Record | None:
    return records[index] if index is not None else None

def format_record(record: Record | None) -> str:
    if record is None:
        return "немає"

    code, name, value, count = record
    return f"{code} | {name} | {value} грамів | {count} од. | {value * count} грамів"

def main():
    n = read_int()
    q = read_int()
    records = read_records(n)
    queries = [read_int() for _ in range(q)]

    accepted, rejected = validate_records(records)
    for message in rejected:
        print(message)
    print(f"Прийнято записів: {len(accepted)}")
    print(f"Відхилено записів: {len(rejected)}")

    by_code = sorted(accepted, key=lambda record: record[0])
    print(f"Коди за зростанням: {format_list([record[0] for record in by_code])}")

    for code in queries:
        linear_index, linear_checked = linear_search(accepted, code)
        binary_index, binary_checked = binary_search(by_code, code)
        linear = pick(accepted, linear_index)
        binary = pick(by_code, binary_index)
        print(f"Запит: {code}")
        print(f"Лінійний: {format_record(linear)}; переглянуто: {linear_checked}")
        print(f"Бінарний: {format_record(binary)}; переглянуто: {binary_checked}")
        print(f"Результати збігаються: {yes_no(linear == binary)}")


if __name__ == "__main__":
    main()
