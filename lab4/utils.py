def format_list(values: list) -> str:
    return " ".join(map(str, values)) if values else "немає"
