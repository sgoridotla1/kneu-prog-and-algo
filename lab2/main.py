"""Варіант 64. Підсилення сигналу з обмеженням."""

from calculations import next_state, state_iterative, state_recursive


def read_int_in_range(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue

        if low <= value <= high:
            return value
        print("Помилка: значення поза допустимим діапазоном.")


def main():
    n = read_int_in_range("Введіть n (0..30): ", 0, 30)
    a = read_int_in_range("Введіть a (0..100): ", 0, 100)
    b = read_int_in_range("Введіть b (1..10): ", 1, 10)
    t = read_int_in_range("Введіть t (0..1000000000): ", 0, 10**9)

    x = a
    total = 0
    first_step = 0 if x >= t else None

    print(f"Початковий стан: {x}")
    if n == 0:
        print("Кроків немає.")
    for i in range(1, n + 1):
        x = next_state(x, i, a, b)
        total += x
        if first_step is None and x >= t:
            first_step = i
        print(f"Стан {i}: {x}")

    result_iterative = state_iterative(n, a, b)
    result_recursive = state_recursive(n, a, b)

    print(f"Результат ітераційно: {result_iterative}")
    print(f"Результат рекурсивно: {result_recursive}")
    same = "так" if result_iterative == result_recursive else "ні"
    print(f"Результати збігаються: {same}")

    print(f"Сума станів після кроків: {total}")
    if first_step is None:
        print("Поріг не досягнуто.")
    else:
        print(f"Перший крок досягнення порога: {first_step}")


if __name__ == "__main__":
    main()
