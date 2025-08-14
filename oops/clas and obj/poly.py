#polymorphism
class movies:
    def __init__(self, name, hero):
        self.name = name
        self.hero = hero
    def title(self): #title is polymorphic method
        print("Movie Title")
class action(movies):
    def title(self):
        print("Action Movie Title")
class comedy(movies):
    def title(self):
        print("Comedy Movie Title")
m = movies("coolie", "Rajnikanth")
a = action("Baasha", "Rajnikanth")
c = comedy("Muthu", "Rajnikanth")
for x in (m, a, c):
    print(x.name)
    print(x.hero)
    x.title()
# method overloading
class operation:
    def add(self,a=0, b=0, *args):
        return a + b + sum(args)
op = operation()
print(op.add())
print(op.add(5, 10))
print(op.add(5, 10, 15))
# method overriding
class payment:
    def pay(self):
        print("Payment method")
class online_payment(payment):
    def pay(self):
        print("Online Payment method")
class cash_payment(payment):
    def pay(self):
        print("Cash Payment method")
p = payment()
o = online_payment()
c = cash_payment()
p.pay()
o.pay()
c.pay()
#operator overloadingclass add:
class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a + self.b)
class concat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return self.a + self.b

c = add(6, 4)
d = concat("Hello, ", "World!")
print(c)
print(d)
