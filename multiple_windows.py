"""Повышенное №8: главное окно и независимые дочерние Toplevel."""

import tkinter as tk
from tkinter import ttk


def open_child(parent: tk.Tk) -> tk.Toplevel:
    """Открыть дочернее окно без второго Tk и второго mainloop."""
    child = tk.Toplevel(parent)
    child.title('Дополнительное окно')
    child.geometry('340x160')
    ttk.Label(child, text='Это самостоятельное дочернее окно.').pack(pady=25)
    ttk.Button(child, text='Закрыть это окно', command=child.destroy).pack()
    return child


def create_window() -> tk.Tk:
    """Создать главное окно с кнопкой открытия новых окон."""
    root = tk.Tk()
    root.title('Несколько окон')
    root.geometry('420x200')
    ttk.Label(root, text='Можно открыть несколько окон одновременно.').pack(
        pady=30,
    )
    ttk.Button(root, text='Новое окно',
               command=lambda: open_child(root)).pack()
    return root


if __name__ == '__main__':
    create_window().mainloop()
