#staticmethod
class Arithmetic:
    @staticmethod
    def add(x,y):
        return x+y
res = Arithmetic.add(5, 10)
print(res)
#classmethod
class car:
    total_cars=0
    def __init__(self, type):
        self.type = type
        car.total_cars += 1
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars
car.get_total_cars()  
car1 = car("Sedan")
car2 = car("SUV")
print(car2.get_total_cars())
print(car.get_total_cars())
#property
class Person:
    def __init__(self, fname, lname):
        self._fname = fname
        self._lname = lname

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

p1 = Person("Leela", "Shree")

print(p1.fname)   
print(p1.lname)  
#property with setter 
class Circle:
    def __init__(self,radius):
        self._radius = radius
    @property
    def radius(self):
        return self._radius
    @property
    def area(self):
        return 3.14*(self._radius**2)
c = Circle(5)
print(c.radius)
print(c.area)
#temperature conversion using property
class temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
t = temperature(25)

print(t.celsius)     
print(t.fahrenheit)   

t.fahrenheit = 212
print(t.celsius)  
#fibonacci    
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
print(fib(10))
#str to obj
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls,person_string):
        name, age = person_string.split("-")
        return cls(name, int(age))
p1 = person.from_string("prat-23")
print(p1.name)  
print(p1.age)   
#odd or even
class MathOperations:
    @staticmethod
    def odd_even(num):
        if num%2 == 0:
            return"even"
        else:
            return"odd"
print(MathOperations.odd_even(10))  
print(MathOperations.odd_even(11))
#rectangle perimeter
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)
r= rectangle(5, 10)
print(r.perimeter)
#mail
class User:
    def __init__(self, name):
        self._name = name
        self._email = f"{name.lower()}@yahoo.com"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._email = f"{value.lower()}@gmail.com"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
u = User("naren")
print(u.email)  
u.name = "Bolucas"
print(u.email)  
u.email = "conrad@outlook.com"
print(u.email)