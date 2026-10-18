def format_ids(ids: list[int]) -> str:
    return " ".join(map(str, ids)) if ids else "-"

def read_commands() -> list[list[str]]:
    n = int(input())
    return [input().split() for _ in range(n)]
