#single inheritance
class animal:
    def eat(self):
        print("animal can Eat")
class cow(animal):
    def sound(self):
        print("Moo")
c = cow()
c.eat()
c.sound()
#multiple inheritance
class lion:
    def roar(self):
        print("Lion can Roar")
class lioness:
    def hunt(self):
        print("Lioness can Hunt")
class club(lion,lioness):
    def play(self):
        print("Club can Play")
l =club()
l.roar()
l.hunt()
l.play()
#multilevel inheritance
class firstgenerationlanguage:
    def first(self):
        print("Machine code")
class secondgenerationlanguage(firstgenerationlanguage):
    def second(assembly):
        print("Assembly code")
class thirdgenerationlanguage(secondgenerationlanguage):
    def third(self):
        print("High level code")
t = thirdgenerationlanguage()
t.first()
t.second()
t.third()
#hierarchical inheritance
class thesummeriturnedpretty:
    def cast(self):
        print("Summer is pretty")
class cornrad(thesummeriturnedpretty):
    def cast_conrad(self):
        print("Conrad is a character")
class jeremiah(thesummeriturnedpretty):
    def cast_jeremiah(self):
        print("Jeremiah is a character")
c = cornrad()
j = jeremiah()
c.cast()
c.cast_conrad()
j.cast_jeremiah()
#hybrid inheritance
class school:
    def name(self):
        print("This is a school")
class student(school):
    def study(self):
        print("Student can Study")
class teacher(school):
    def teach(self):
        print("Teacher can Teach")
class principal(student, teacher):
    def manage(self):
        print("Principal can Manage")
obj = principal()
obj.study()
obj.teach()