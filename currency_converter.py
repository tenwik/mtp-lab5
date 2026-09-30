"""Повышенное №6: конвертер с фиксированными учебными курсами."""

from decimal import Decimal, InvalidOperation, localcontext
import tkinter as tk
from tkinter import ttk

RATES = {'RUB': Decimal('1'), 'USD': Decimal('90'), 'EUR': Decimal('100')}


def convert(amount: str, source: str, target: str) -> Decimal:
    """Перевести неотрицательную сумму по учебному курсу через рубль."""
    if source not in RATES or target not in RATES:
        raise ValueError('Выберите валюту из списка.')
    try:
        value = Decimal(amount.strip().replace(',', '.'))
    except InvalidOperation as error:
        raise ValueError('Введите число.') from error
    if not value.is_finite() or value < 0 or value > Decimal('1e12'):
        raise ValueError('Сумма должна быть от 0 до 1 000 000 000 000.')
    with localcontext() as context:
        context.prec = 32
        return (value * RATES[source] / RATES[target]).quantize(Decimal('.01'))


def create_window() -> tk.Tk:
    """Создать форму конвертера с сообщениями об ошибках ввода."""
    root = tk.Tk()
    root.title('Конвертер валют')
    root.geometry('520x310')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    ttk.Label(frame, text='Учебные курсы: USD = 90 RUB; EUR = 100 RUB.').pack()
    ttk.Label(frame, text='Курсы фиксированные, не рыночные.').pack(pady=5)
    amount = tk.StringVar(value='100')
    source = tk.StringVar(value='RUB')
    target = tk.StringVar(value='USD')
    result = tk.StringVar(value='')
    ttk.Label(frame, text='Сумма').pack(anchor='w')
    ttk.Entry(frame, textvariable=amount).pack(fill='x')
    for caption, variable in (('Из валюты', source), ('В валюту', target)):
        ttk.Label(frame, text=caption).pack(anchor='w')
        ttk.Combobox(frame, textvariable=variable, values=list(RATES),
                     state='readonly').pack(fill='x')

    def calculate() -> None:
        """Отобразить результат или понятную ошибку."""
        try:
            result.set(f'{convert(amount.get(), source.get(), target.get())}'
                       f' {target.get()}')
        except ValueError as error:
            result.set(str(error))

    ttk.Button(frame, text='Перевести', command=calculate).pack(pady=10)
    ttk.Label(frame, textvariable=result).pack()
    return root


if __name__ == '__main__':
    create_window().mainloop()
