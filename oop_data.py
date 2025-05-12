from abc import ABC, abstractmethod
from typing import Callable

"""
💡 1. Metaclasses e Classes Abstratas
Metaclasses:
Metaclasses são "classes de classes" que definem como as classes se comportam. Você pode pensar nelas como "fábricas de classes".

Por que usar?
Controle sobre a criação de classes.

Modificação dinâmica de classes.

Exemplo de Metaclasse:
""" # noqa501


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def log(self, message: str):
        print(f"[LOG] {message}")


logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)


"""
Classes Abstratas:
Usamos classes abstratas para definir métodos que devem ser implementados por subclasses.

Exemplo:
""" # noqa501


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"


dog = Dog()
print(dog.make_sound())


"""
🧩 2. Design Patterns em Python
Singleton:
Já vimos na metaclasse. Garante que uma classe tenha apenas uma instância.

Factory:
Cria objetos sem especificar a classe exata que será instanciada.

Exemplo:
""" # noqa501


class Car(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass


class Sedan(Car):
    def drive(self) -> str:
        return "Driving a sedan!"


class SUV(Car):
    def drive(self) -> str:
        return "Driving an SUV!"


class CarFactory:
    @staticmethod
    def create_car(car_type: str) -> Car:
        if car_type == "sedan":
            return Sedan()
        elif car_type == "suv":
            return SUV()
        raise ValueError("Unknown car type")


car = CarFactory.create_car("suv")
print(car.drive())


"""
Strategy:
Permite alterar o comportamento de um objeto em tempo de execução.

Exemplo:
""" # noqa501


class Calculator:
    def __init__(self, strategy: Callable[[int, int], int]):
        self.strategy = strategy

    def calculate(self, a: int, b: int) -> int:
        return self.strategy(a, b)


def add(x, y): return x + y
def subtract(x, y): return x - y


calc = Calculator(add)
print(calc.calculate(10, 5))

calc.strategy = subtract
print(calc.calculate(10, 5))


"""
🔄 3. Sobrecarga de Operadores
A sobrecarga de operadores permite que objetos personalizados se comportem de maneira semelhante a tipos nativos.

Exemplo de Sobrecarga:
""" # noqa501


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
