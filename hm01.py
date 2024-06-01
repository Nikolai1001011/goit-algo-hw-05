def caching_fibonacci():
    # Словник для зберігання кешу значень чисел Фібоначчі
    cache = {}
    def fibonacci(n):
        # Базові випадки: якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо значення вже є в кеші, повертаємо його
        elif n in cache:
            return cache[n]
        else:
            # якщо число не в кеші, зберігаємо в кеші і повертаємо
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(17))
print(fib(10))
