class sbi:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
b1 =sbi("dim",123456789, 10000)
b2 =sbi("jim",987654321, 20000)
print(b1.acc_no)
print(b2.balance)

class student:
    def __init__(self, name, roll_no,college):
        self.name = name
        self.roll_no = roll_no
        self.college = college
s1 = student("digu", 101, "smvec")
s2 = student("pinku", 102, "pec")
s3 = student("Chae", 103, "MIT")
print(s1.name)
print(s2.roll_no)
print(s3.college)

class series:
    def __init__(self):
        self.name ="wednesday"
        self.cast = "jenna ortega"
        self.season = 2
s = series()
print(s.name)
print(s.cast)
print(s.season)
        

class pm:
    def __init__(self, name, year):
        self.name = name
        self.year = year
p1 = pm("modi", 2014)
print(p1.name)
print(p1.year)