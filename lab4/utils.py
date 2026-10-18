def format_list(values: list) -> str:
    return " ".join(map(str, values)) if values else "немає"

def read_int() -> int:
    return int(input())

def read_int_list(count: int) -> list[int]:
    """рядок читається завжди, навіть порожній за count = 0"""
    values = [int(item) for item in input().split()]
    return values[:count]
