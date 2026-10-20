import math
from abc import ABC, abstractmethod


# ==========================================
# 1. Инкапсуляция
# ==========================================
class Person:
    def __init__(self):
        self._age = 0  # Приватный (защищенный) атрибут

    def set_age(self, age: int):
        """Устанавливает возраст с проверкой на отрицательное значение."""
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = age

    def get_age(self) -> int:
        """Возвращает текущий возраст."""
        return self._age


# ==========================================
# 2. Наследование
# ==========================================
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "I am an animal"


class Dog(Animal):
    def speak(self) -> str:
        return "Woof"


class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


# ==========================================
# 3. Полиморфизм
# ==========================================
class Vehicle:
    def move(self) -> str:
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self) -> str:
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self) -> str:
        return "Bicycle is pedaling"


def move(vehicle: Vehicle) -> str:
    """Функция принимает любой транспорт и вызывает его метод move()."""
    return vehicle.move()


# ==========================================
# 4. Абстракция
# ==========================================
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Абстрактный метод для вычисления площади."""
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


# ==========================================
# Демонстрация работы (Примеры использования)
# ==========================================
if __name__ == "__main__":
    print("--- 1. Инкапсуляция ---")
    p = Person()
    p.set_age(25)
    print(p.get_age())  # Вывод: 25
    try:
        p.set_age(-5)  # Ожидается ошибка
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n--- 2. Наследование ---")
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak())  # Вывод: Buddy Woof
    print(cat.name, cat.speak())  # Вывод: Kitty Meow

    print("\n--- 3. Полиморфизм ---")
    car = Car()
    bike = Bicycle()
    print(move(car))   # Вывод: Car is driving
    print(move(bike))  # Вывод: Bicycle is pedaling

    print("\n--- 4. Абстракция ---")
    rect = Rectangle(10, 5)
    circle = Circle(7)
    print(rect.area())  # Вывод: 50
    print(round(circle.area(), 2))  # Вывод: ~153.94
