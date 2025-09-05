#Static methods
#__init__ method
# __str__method
# multiply useable of class method student



class Student:
    def __init__(self,name, marks,subjects):
        self.name = name
        self.marks = marks
        self.subjects = subjects

    def __str__(self):
        return f"He got {self.name} grade "

    def final_marks(self):
        if self.marks / self.subjects > 85:
            print("Results : Grade A+")
        elif self.marks / self.subjects > 75:
            print("Results : Grade A")
        elif self.marks / self.subjects > 65:
            print("Results : Grade B+")
        elif self.marks / self.subjects > 55:
            print("Results : Grade C+")
        elif self.marks / self.subjects > 40:
            print("Results : Grade C")
        else:
            print("Results: fail")

    @staticmethod
    def grades(marks, subjects):
        results = marks/subjects
        return results



result = Student("john", 379, 4)
result1 = Student("david", 280, 4)
result3 = Student("Ochieng", 140, 4)

print( f"{result.name} has got {Student.grades(379,4)}%")
result.final_marks()
print( f"{result1.name} has got {Student.grades(280,4)}%")
result1.final_marks()
print( f"{result3.name} has got {Student.grades(140,4)}%")

result3.final_marks()






#multiply polymorphism/ multiply inheritances/ class attributes or methods/ modifying objects data
#Comprehension

class Transport:
    def __init__(self, name, brand, year):
        self.brand=brand
        self.name=name
        self.year = year


class Car(Transport):
    def __init__(self, types, name,brand, year, mean_transport):
        super(). __init__(brand, name, year)
        self.mean_transport = mean_transport
        self.types = types

    def moving(self):
        print(f"The {self.types} is  a mean of {self.mean_transport} transport")
        print("it's the cheapest means of transport in the world")
        print(f"{self.name} is a example of {self.types} used in {self.mean_transport} transport")

class Boat(Transport):
    def __init__(self, types ,name, brand, year, mean_transport):
        super(). __init__(name, brand, year)
        self.mean_transport = mean_transport
        self.types = types

    def moving(self):
        print(f"The {self.types} is a mean of {self.mean_transport}  transport")
        print("it's less and manageable afford, most often use alot on lakes and rivers areas")
        print(f"{self.name} is a example of {self.types} used in {self.mean_transport} transport")


class Aeroplane(Transport):
    def __init__(self,types, name, brand, year, mean_transport):
        super(). __init__(name, brand, year)
        self.mean_transport = mean_transport
        self.types = types


    def moving(self):
        print(f"The {self.types} is a mean of {self.mean_transport}  transport")
        print("It's the most expensive means of transport")
        print(f"{self.name} is a example of {self.types} used in {self.mean_transport} transport")


C = Car("car","hyundai ", "electra Sel ", 2023, "Road")
b = Boat("Boat","four winns", "sea roy", 1990, "water")
a = Aeroplane("Airplane","spirit airlines", "spirits", 1980, "Air")

for i in [C, b, a]:
    print(" \n-----------------------------TRANSPORT----------------------------------------")
    print(i.types)
    i.moving()


