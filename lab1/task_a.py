"""Варіант 69. Завдання А: Пекарня."""

import math


def main():
    try:
        m = float(input("Введіть масу тіста m (кг): "))
        p = float(input("Введіть втрату маси p (%): "))
        n = int(input("Введіть кількість виробів n: "))
    except ValueError:
        print("Помилка: m і p мають бути числами, а n — цілим числом.")
        return

    if not (math.isfinite(m) and math.isfinite(p) and m > 0 and 0 <= p < 100 and n > 0):
        print("Помилка: потрібно m > 0, 0 ≤ p < 100, n > 0.")
        return

    g = m * (1 - p / 100)
    u = g / n
    print(f"g={g:.2f} кг; u={u:.2f} кг.")


if __name__ == "__main__":
    main()
