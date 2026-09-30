"""Среднее №7: меню File с командой Exit."""

import tkinter as tk
from tkinter import ttk


def create_window() -> tk.Tk:
    """Создать окно, закрываемое командой меню."""
    root = tk.Tk()
    root.title('Меню приложения')
    root.geometry('380x180')
    menu = tk.Menu(root, name='menubar')
    file_menu = tk.Menu(menu, tearoff=False, name='file')
    file_menu.add_command(label='Exit', command=root.destroy)
    menu.add_cascade(label='File', menu=file_menu)
    root.configure(menu=menu)
    ttk.Label(root, text='Для выхода выберите File → Exit.').pack(pady=50)
    return root


if __name__ == '__main__':
    create_window().mainloop()
