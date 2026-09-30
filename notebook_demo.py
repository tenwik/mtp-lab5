"""Среднее №5: окно с вкладками ttk.Notebook."""

import tkinter as tk
from tkinter import ttk


def create_window() -> tk.Tk:
    """Создать окно с двумя независимыми вкладками."""
    root = tk.Tk()
    root.title('Вкладки')
    root.geometry('440x240')
    notebook = ttk.Notebook(root, name='notebook')
    notebook.pack(fill='both', expand=True, padx=12, pady=12)
    for title, text in (
        ('Главная', 'Пример интерфейса с вкладками'),
        ('О программе', 'Лабораторная работа №5. Вариант 5.'),
    ):
        frame = ttk.Frame(notebook, padding=20)
        ttk.Label(frame, text=text).pack(anchor='w')
        notebook.add(frame, text=title)
    return root


if __name__ == '__main__':
    create_window().mainloop()
