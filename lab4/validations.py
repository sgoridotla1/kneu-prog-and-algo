def read_int_in_range(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue

        if low <= value <= high:
            return value
        print("Помилка: значення поза допустимим діапазоном.")

def read_int_list(prompt: str, count: int, low: int, high: int) -> list[int]:
    if count == 0:
        return []

    while True:
        try:
            values = [int(item) for item in input(prompt).split()]
        except ValueError:
            print("Помилка: потрібно ввести цілі числа.")
            continue

        if len(values) != count:
            print(f"Помилка: потрібно ввести рівно {count} чисел.")
            continue
        if not all(low <= value <= high for value in values):
            print("Помилка: значення поза допустимим діапазоном.")
            continue
        return values
