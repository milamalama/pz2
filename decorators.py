import time
import functools

def timer(func):
    """Декоратор для измерения времени выполнения функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Функция {func.__name__} выполнена за {end - start:.4f} сек.")
        return result
    return wrapper


def debug(func):
    """Декоратор для вывода аргументов и результата функции."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызов {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} вернула {result!r}")
        return result
    return wrapper


def limit_calls(max_calls=5):
    """
    Декоратор, ограничивающий количество вызовов функции.
    После превышения лимита вызывает исключение.
    """
    def decorator(func):
        func.calls = 0  # хранит счётчик вызовов как атрибут функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if func.calls >= max_calls:
                raise RuntimeError(f"Функция {func.__name__} превысила лимит вызовов ({max_calls})")
            func.calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
