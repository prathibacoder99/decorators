#encapsulation
class Car:
    def __init__(self, brake, accelerate, speed):
        self.brake = brake # public attribute             
        self._accelerate = accelerate # protected attribute
        self.__speed = 0                
        self.set_speed(speed) # private attribute          

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("Speed must be positive")

c = Car("Disc Brake", "Fast", -1)

print(c.get_speed())   
print(c._accelerate)  
print(c.brake)         