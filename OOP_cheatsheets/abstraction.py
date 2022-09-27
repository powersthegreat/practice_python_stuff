# When a program starts to get big, classes might 
# start to share functionality or we may lose sight 
# of the purpose of a class’s inheritance structure. 
# In order to alleviate issues like this, we can use 
# the concept of abstraction.

# Abstraction helps with the design of code by 
# defining necessary behaviors to be implemented 
# within a class structure. By doing so, abstraction 
# also helps avoid leaving out or overlapping class 
# functionality as class hierarchies get larger.

from abc import ABC, abstractmethod
 
class Animal(ABC):
  def __init__(self, name):
    self.name = name
 
  @abstractmethod
  def make_noise(self):
    pass
 
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))
 
kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"

##############################################

from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
    def say_id(self):
      print(self.id)

e1 = Employee()
e1.say_id()