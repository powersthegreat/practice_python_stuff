# In computer programming, polymorphism is the ability to apply
# an identical operation onto different types of objects. This 
# can be useful when an object type may not be known at the program
# runtime. Polymorphism can be applied using Python in multiple ways.
# We have already experienced a form of it when exploring inheritance.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Robot:
 
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")

an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()
 
# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"
################################################################

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
e1 = Employee()
e2 = Admin()
e3 = Manager()
meeting = [e1, e2, e3]

for employee in meeting:
  employee.say_id()