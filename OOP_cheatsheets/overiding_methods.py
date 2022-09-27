# When implementing inheritance, a child class may want 
# to change the behavior of a method from its parent 
# class. In Python, all we have to do is override a method 
# definition. An overridden method in a subclass is one 
# that has the same definition as the parent class but 
# contains different behavior.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))

class Cat(Animal):
  #overides the parents make_noise method
  def make_noise(self):
    print("{} says, Meow!".format(self.name))

pet1 = Animal("Rex")
pet1.make_noise() #Prints: Rex says, Grrrr
 
pet2 = Cat("Maisy")
pet2.make_noise() #Prints: Maisy says, Meow!

########################################################
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  #overides parents 'say_id' method
  def say_id(self):
    print("I am an Admin.")
  

e1 = Employee()
e2 = Employee()
e3 = Admin()
e1.say_id() #Prints: My id is 1.
e2.say_id() #Prints: My id is 2.
e3.say_id() #Prints: I am an Admin.
