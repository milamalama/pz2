import math
from decorators import timer, debug
from calculations import linear, quadratic, sine, exponential, logarithm
from visualization import plot_function, print_table

# Словарь доступных функций
FUNCTIONS = {
    "1": ("линейная (2x + 3)", linear),
    "2": ("квадратичная (x² - 4x + 3)", quadratic),
    "3": ("синус", sine),
    "4": ("экспонента", exponential),
    "5": ("натуральный логарифм", logarithm),}


def get_user_input():
    print("Доступные функции:")
    for key, (desc, _) in FUNCTIONS.items():
        print(f"{key}. {desc}")

    choice = input("\nВыберите номер функции: ").strip()
    if choice not in FUNCTIONS:
        raise ValueError("Неверный выбор функции!")

    a = float(input("Введите начало отрезка (a): "))
    b = float(input("Введите конец отрезка (b): "))
    if a >= b:
        raise ValueError("a должно быть меньше b!")

    step = float(input("Введите шаг: "))
    if step <= 0:
        raise ValueError("Шаг должен быть положительным!")

    return choice, a, b, step


@timer
@debug
def compute_xy(func, a, b, step):
    x_vals = []
    y_vals = []
    x = a
    while x <= b:
        x_vals.append(x)
        try:
            y_vals.append(func(x))
        except ValueError as e:
            print(f"Ошибка при x = {x}: {e}")
            y_vals.append(float('nan'))  # или пропустить
        x += step
    return x_vals, y_vals


def main():
    try:
        choice, a, b, step = get_user_input()
        func_name, func = FUNCTIONS[choice]
        print(f"\nВы выбрали функцию: {func_name}\n")

        x_vals, y_vals = compute_xy(func, a, b, step)

        print("\nТаблица значений:")
        print_table(x_vals, y_vals)

        print("\nГрафик функции:")
        plot_function(x_vals, y_vals, a, b)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()