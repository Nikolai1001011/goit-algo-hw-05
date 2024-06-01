import re
from typing import Callable

#Функція, яка створює генератор для ідентифікації дійсних чисел у тексті.
def generator_numbers(text: str): 
    # Компілюємо регулярний вираз для пошуку дійсних чисел
    pattern = re.compile(r' \\d+\.\\d+ | \\d+ ')
    
    # Знаходимо всі збіги у тексті
    matches = pattern.finditer(text)
    
    # Проходимося по кожному збігу і повертаємо його як дійсне число
    for match in matches:
        yield float(match.group())

#Функція, яка підсумовує всі числа, знайдені у тексті за допомогою генератора.
def sum_profit(text: str, func: Callable):
    
    # Викликаємо генератор, щоб отримати числа
    numbers = func(text)
    
    # Підсумовуємо всі числа
    total = sum(numbers)
    
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")