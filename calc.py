#!/usr/bin/env python3
import os
from style import colors, print_header, print_result, print_error


def calculator():
    """Главная функция калькулятора"""
    os.system('clear' if os.name == 'posix' else 'cls')
    print_header()

    while True:
        print(f"\n{colors['yellow']}Выберите действие:{colors['reset']}")
        print(f"  {colors['green']}1.{colors['reset']} Сложение       {colors['green']}2.{colors['reset']} Вычитание")
        print(f"  {colors['green']}3.{colors['reset']} Умножение      {colors['green']}4.{colors['reset']} Деление")
        print(f"  {colors['green']}5.{colors['reset']} Выход")

        choice = input(f"\n{colors['cyan']}Введите номер действия: {colors['reset']}")

        if choice == '5':
            print(f"\n{colors['purple']} До свидания! Спасибо, что пользовались калькулятором!{colors['reset']}")
            break

        if choice not in ['1', '2', '3', '4']:
            print_error("Неверный выбор! Попробуйте снова.")
            continue

        try:
            num1 = float(input(f"{colors['cyan']}Введите первое число: {colors['reset']}"))
            num2 = float(input(f"{colors['cyan']}Введите второе число: {colors['reset']}"))
        except ValueError:
            print_error("Это не число! Введите цифры.")
            continue

        if choice == '1':
            result = num1 + num2
            operator = '+'
        elif choice == '2':
            result = num1 - num2
            operator = '-'
        elif choice == '3':
            result = num1 * num2
            operator = '*'
        elif choice == '4':
            if num2 == 0:
                print_error("На ноль делить нельзя!")
                continue
            result = num1 / num2
            operator = '/'

        print_result(num1, num2, operator, result)


if __name__ == "__main__":
    calculator()
