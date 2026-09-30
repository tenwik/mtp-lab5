"""Проверки настоящих Tk-виджетов; требуется графическая сессия."""

import tkinter as tk
import unittest

import currency_converter
import hello_demo
import menu_demo
import multiple_windows
import notebook_demo


class GuiTests(unittest.TestCase):
    """Проверить события и жизненный цикл окон."""

    def test_tabs(self) -> None:
        """Вторая вкладка выбирается."""
        root = notebook_demo.create_window()
        self.addCleanup(root.destroy)
        root.withdraw()
        notebook = root.nametowidget('notebook')
        self.assertEqual(len(notebook.tabs()), 2)
        notebook.select(1)
        root.update_idletasks()
        self.assertEqual(notebook.index(notebook.select()), 1)

    def test_greeting(self) -> None:
        """Нажатие кнопки обновляет надпись."""
        root = hello_demo.create_window()
        self.addCleanup(root.destroy)
        root.withdraw()
        root.nametowidget('hello').invoke()
        self.assertEqual(
            root.nametowidget('greeting').cget('text'), 'Привет, Георгий!'
        )

    def test_exit(self) -> None:
        """Команда File → Exit уничтожает окно."""
        root = menu_demo.create_window()
        root.withdraw()
        root.nametowidget('menubar.file').invoke(0)
        with self.assertRaises(tk.TclError):
            root.winfo_exists()

    def test_child_windows(self) -> None:
        """Закрытие дочернего окна не закрывает остальные."""
        root = multiple_windows.create_window()
        self.addCleanup(root.destroy)
        root.withdraw()
        first = multiple_windows.open_child(root)
        second = multiple_windows.open_child(root)
        first.withdraw()
        second.withdraw()
        first.destroy()
        self.assertTrue(root.winfo_exists())
        self.assertTrue(second.winfo_exists())

    def test_converter_window(self) -> None:
        """Форма конвертера создаётся в реальном Tk."""
        root = currency_converter.create_window()
        self.addCleanup(root.destroy)
        root.withdraw()
        root.update_idletasks()
        self.assertEqual(root.title(), 'Конвертер валют')


if __name__ == '__main__':
    unittest.main()
