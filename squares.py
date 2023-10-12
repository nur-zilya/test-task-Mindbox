import math

class GeometryLibrary:
    @staticmethod
    def circle_area(radius):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным")
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Длины сторон должны быть положительными числами")
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        sides.sort()
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)

if __name__ == "__main__":
    # Пример использования библиотеки
    radius = 5.0
    circle_area = GeometryLibrary.circle_area(radius)
    print(f"Площадь круга с радиусом {radius} = {circle_area}")

    side1 = 3.0
    side2 = 4.0
    side3 = 5.0
    triangle_area = GeometryLibrary.triangle_area(side1, side2, side3)
    print(f"Площадь треугольника с сторонами {side1}, {side2}, {side3} = {triangle_area}")

    is_right = GeometryLibrary.is_right_triangle(side1, side2, side3)
    if is_right:
        print("Этот треугольник - прямоугольный")
    else:
        print("Этот треугольник - не прямоугольный")
