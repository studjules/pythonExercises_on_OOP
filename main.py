#Object oriented programming

class Student:
    def __init__(self, name, age, grade):
        self.name =name
        self.age =age
        self.grade= grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name =name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students)< self.max_students:
            self.students.append(student)
            return True
        return "Course is full"

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            average = value/len(self.students)
            return average

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course= Course("Science",2)

course.add_student(s1)
course.add_student(s2)
print(course.add_student(s3))
print(course.get_average_grade())

class Katze():
    def __init__(self, age, name="harri"):
        self.name = name
        self.age = age


c1=Katze(2)
# Neuer Bauplan für eine Person:
# Beim Erstellen eines Objekt der Klasse Person
# werden die Instanzvariablen direkt definiert.
class Person:
    def __init__(self, name, vorname, geb_datum, gewicht):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.gewicht = gewicht

    def vorstellen(self):
        text = "Hallo.\nIch heisse " \
               + self.vorname + " " \
               + self.name + ", wiege " \
               + str(self.gewicht) + " kg und habe am " \
               + self.geb_datum + " Geburtstag.\n"\
               + "Nice to meet you."
        print(text)

p1=Person("Müller", "Hans", "01.01.2000", 80)

p1.vorstellen()

class persona():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email= first+"."+last+"@gmail.com"


    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @email.setter
    def email(self,email):
        first, last = email.split("@")[0].split(".")
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


    @fullname.setter
    def fullname(self,name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("delete name")
        self.first = None
        self.last = None



pe1=persona("John", "jack")
print(pe1.email)
pe1=persona("John", "jück")
print(pe1.email)

del pe1.fullname
print(pe1.fullname)

pe1.fullname = "Tim Tom"
print(pe1.fullname)
print(pe1.email)