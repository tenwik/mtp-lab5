"""Проверки расчётов и недопустимых сумм конвертера."""

import unittest
from decimal import Decimal

from currency_converter import convert


class CurrencyTests(unittest.TestCase):
    """Проверить курсы, округление и валидацию."""

    def test_conversion(self) -> None:
        """Конвертировать в обе стороны и между валютами."""
        self.assertEqual(convert('90', 'RUB', 'USD'), Decimal('1.00'))
        self.assertEqual(convert('1,5', 'EUR', 'RUB'), Decimal('150.00'))
        self.assertEqual(convert('10', 'USD', 'EUR'), Decimal('9.00'))
        self.assertEqual(convert('0', 'RUB', 'USD'), Decimal('0.00'))
        self.assertEqual(convert('1', 'RUB', 'RUB'), Decimal('1.00'))

    def test_invalid_values(self) -> None:
        """Отклонять нечисловые, отрицательные и бесконечные суммы."""
        for amount in ('', 'abc', '-1', 'NaN', 'Infinity', '1e100'):
            with self.subTest(amount=amount), self.assertRaises(ValueError):
                convert(amount, 'RUB', 'USD')
        with self.assertRaises(ValueError):
            convert('10', 'XYZ', 'USD')


if __name__ == '__main__':
    unittest.main()
