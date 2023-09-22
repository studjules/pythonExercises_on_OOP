class Pet: #parent
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I dont know what to say")

class Cat(Pet): #child
    def __init__(self,name,age,color):
        super().__init__(name,age) #inherit the initialization
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet): #child
    def speak(self):
        print("Bark")

class Fish(Pet): #child
    pass

p= Pet("Tim", 19)
p.show()
c= Cat("Bill", 34, "Brown")
c.show()
d = Dog("Jill",25)
d.speak()
f=Fish("Bubbles",10)
f.speak()