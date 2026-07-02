# Цвета для терминала
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m',
    'bold': '\033[1m'
}

def print_header():
    """Печатает красивый заголовок"""
    print(f"""
{colors['cyan']}{'═' * 50}
{colors['bold']}{colors['purple']}   КАЛЬКУЛЯТОР С ДИЗАЙНОМ  
{colors['reset']}{colors['cyan']}{'═' * 50}
{colors['reset']}
    """)

def print_result(num1, num2, operator, result):
    """Печатает результат с красивым форматированием"""
    print(f"""
{colors['green']}{'─' * 40}
{colors['bold']}   📊  РЕЗУЛЬТАТ:
{colors['reset']}
   {colors['yellow']}{num1} {operator} {num2} = {colors['bold']}{colors['cyan']}{result}{colors['reset']}
{colors['green']}{'─' * 40}{colors['reset']}
    """)

def print_error(message):
    """Печатает ошибку красным цветом"""
    print(f"\n{colors['red']}❌ ОШИБКА: {message}{colors['reset']}\n")