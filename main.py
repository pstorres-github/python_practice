# classes

# capitalize first letter of every word (Pascal case)
class Mammal:
    # initialize the object (constructor)
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walk")

    def printName(self):
        return(self.name)


# need two line breaks between classes!!
# inheritance.  Both dog and cat class are inheriting from Mammal Class
class Dog(Mammal):
    def bark(self):
        print("bark")

# if no added functions, then pass
class Cat(Mammal):
    def meow(self):
        print("meow")


# if no added functions, then pass
class Cow(Mammal):
    pass


# create object
dog = Dog("Cassie")
print("Hello", dog.printName())
dog.walk()

cat = Cat("Silly")
print("Hello", cat.printName())
cat.meow()

cow = Cow("Moo cow")
print("Hello", cow.printName())
