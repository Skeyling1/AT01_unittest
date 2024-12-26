import unittest
from main import add, subtract, multiply, divide, even, reminder_from_division


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)


    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertNotEqual(subtract(5, 2), 9)


    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertNotEqual(multiply(3, 7), 9)


    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertNotEqual(divide(3, 7), 9)


    def even(self):
        self.assertTrue(even(6))


    #Написать функцию для вычисления остатка от деления и тесты для проверки её работы, включая обработку деления на ноль
    def reminder_from_division(self):
        self.assertEqual(reminder_from_division(5, 3), 2)
        self.assertRaises(ValueError, reminder_from_division, 6, 0)








if __name__ == "__main__":
    unittest.main