"""Среднее №1: окно с кнопкой «Привет»."""

import tkinter as tk
from tkinter import ttk


def create_window() -> tk.Tk:
    """Создать кнопку, показывающую приветствие при нажатии."""
    root = tk.Tk()
    root.title('Приветствие')
    root.geometry('380x180')
    label = ttk.Label(root, name='greeting', text='Нажмите кнопку.')
    label.pack(pady=25)
    ttk.Button(
        root, name='hello', text='Привет',
        command=lambda: label.configure(text='Привет, Георгий!'),
    ).pack()
    return root


if __name__ == '__main__':
    create_window().mainloop()
