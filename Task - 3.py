# Task: 3 Создайте класс "Правильная Дробь" и реализуйте методы сравнения, сложения,
# вычитания и умножения для экземпляров этого класса. Не забудьте про сокращение дроби.
from math import gcd


class ProperFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common_factor = gcd(numerator, denominator)
        self.numerator = numerator // common_factor
        self.denominator = denominator // common_factor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Unsupported type for equality comparison.")
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Unsupported type for less than comparison.")
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self == other or self < other

    def __add__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Unsupported type for addition.")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Unsupported type for subtraction.")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Unsupported type for multiplication.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def reduce_fraction(self):
        common_factor = gcd(self.numerator, self.denominator)
        self.numerator //= common_factor
        self.denominator //= common_factor
        return self


if __name__ == "__Task - 3__":

    fraction1 = ProperFraction(3, 5)
    fraction2 = ProperFraction(2, 3)

    print("Fraction 1:", fraction1)
    print("Fraction 2:", fraction2)

    sum_fraction = fraction1 + fraction2
    print("Sum:", sum_fraction)

    difference_fraction = fraction1 - fraction2
    print("Difference:", difference_fraction)

    product_fraction = fraction1 * fraction2
    print("Product:", product_fraction)

    reduced_fraction1 = fraction1.reduce_fraction()
    reduced_fraction2 = fraction2.reduce_fraction()

    print("Reduced Fraction 1:", reduced_fraction1)
    print("Reduced Fraction 2:", reduced_fraction2)


