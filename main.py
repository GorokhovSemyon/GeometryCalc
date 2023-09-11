import unittest
import math

# Импортируем наши классы из библиотеки
from calcClass import Circle, Triangle

class TestGeometryLibrary(unittest.TestCase):

    def test_circle_area(self):
        # Проверяем вычисление площади круга
        circle = Circle(5)
        expected_area = math.pi * 5**2
        self.assertAlmostEqual(circle.area(), expected_area, places=6)

    def test_triangle_area(self):
        # Проверяем вычисление площади треугольника
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0  # Площадь прямоугольного треугольника
        self.assertEqual(triangle.area(), expected_area)

    def test_invalid_circle_args(self):
        # Проверяем, что создание круга с недопустимым количеством аргументов вызывает TypeError
        with self.assertRaises(TypeError):
            invalid_circle = Circle(1, 2)  # Круг с недопустимым количеством аргументов

    def test_invalid_triangle_args(self):
        # Проверяем, что создание треугольника с недопустимым количеством аргументов вызывает TypeError
        with self.assertRaises(TypeError):
            invalid_triangle = Triangle(1, 2)  # Треугольник с недопустимым количеством аргументов

    def test_invalid_value_args_tri(self):
        # Проверяем, что создание треугольника с отрицательным аргументом вызывает ValueError
        with self.assertRaises(ValueError):
            invalid_triangle = Triangle(-2, 3, 4)  # Треугольник с отрицательным аргументом

    def test_invalid_value_args_cir(self):
        # Проверяем, что создание круга с отрицательным аргументом вызывает ValueError
        with self.assertRaises(ValueError):
            invalid_triangle = Circle(-1)  # Круг с отрицательным аргументом

    def test_negative_circle_radius(self):
        # Проверяем, что создание круга с отрицательным радиусом вызывает ValueError
        with self.assertRaises(ValueError):
            negative_circle = Circle(-2.5)

if __name__ == '__main__':
    unittest.main()
