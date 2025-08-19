# abs.py
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, hours, rate):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self, hours, rate):
        
        return f"Full-time employee salary: {rate}"

class PartTimeEmployee(Employee):
    def calculate_salary(self, hours, rate):
        
        return f"Part-time employee salary: {hours * rate}"
f = FullTimeEmployee()
print(f.calculate_salary(8, 5000))   
p = PartTimeEmployee()
print(p.calculate_salary(7, 2000)) 

#payment system

from abc import ABC, abstractmethod
class payment_system(ABC):
    @property
    @abstractmethod
    def process_payment(self):
        pass
class credit_card_payment(payment_system):
    @property
    def process_payment(self):
        return "Processing payment through credit card"
class paypal_payment(payment_system):
    @property
    def process_payment(self):
        return "Processing payment through PayPal"
c = credit_card_payment()
print(c.process_payment)
p = paypal_payment()
print(p.process_payment)