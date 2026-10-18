type Record = tuple[int, str, int, int]

def read_int() -> int:
    return int(input())

def parse_record(line: str) -> Record:
    code, name, value, count = line.split(";")
    return int(code), name, int(value), int(count)

def read_records(count: int) -> list[Record]:
    return [parse_record(input()) for _ in range(count)]

def format_list(values: list) -> str:
    return ", ".join(map(str, values)) if values else "немає"

def yes_no(flag: bool) -> str:
    return "так" if flag else "ні"
