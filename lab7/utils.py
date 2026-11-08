def format_ids(ids: list[int]) -> str:
    return " ".join(map(str, ids)) if ids else "-"
