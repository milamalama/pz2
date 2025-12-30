import matplotlib.pyplot as plt
from tabulate import tabulate

def plot_function(x_vals, y_vals, a, b):
    """Строит график функции по векторам x_vals, y_vals на отрезке [a, b]."""
    plt.figure(figsize=(10, 5))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b')
    plt.title(f"График функции на отрезке [{a}, {b}]")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.xlim(a, b)
    plt.show()

def print_table(x_vals, y_vals):
    """Выводит таблицу X и Y в две строки с учётом разрядности."""
    x_str = ["{:.4f}".format(x) for x in x_vals]
    y_str = ["{:.4f}".format(y) for y in y_vals]
    table = [["X"] + x_str, ["Y"] + y_str]
    print(tabulate(table, headers="firstrow", tablefmt="pretty"))
