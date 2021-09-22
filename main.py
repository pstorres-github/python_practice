# import each class from package
from animals.Mammal import Dog, Cat, Cow
from Dice import Dice
from pathlib import Path

# --------------------------------
dog = Dog("Cassie")
print("Hello", dog.printName())
dog.walk()

cat = Cat("Silly")
print("Hello", cat.printName())
cat.meow()

cow = Cow("Moo cow")
print("Hello", cow.printName())
# -----------------------------------

print("")
print("Dice roll activity")
dice = Dice()
dice.roll()

# ------------------------------------

print("")
print("search for all python files")

path = Path()
for file in path.glob('*.py'): # search for all files in the current path with extension *.py
    print(file)

# ---------------------------------
# installing packages
# terminal command: pip install "package", for example pip install openpyxl

