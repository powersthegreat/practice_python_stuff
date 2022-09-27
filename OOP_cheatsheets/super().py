# When overriding methods we sometimes want to still access 
# the behavior of the parent method. In order to do that we 
# need a way to call the method of the parent class. Python 
# gives us a way to do that using super().

# super() gives us a proxy object. With this proxy object, 
# we can invoke the method of an object’s parent class 
# (also called its superclass). We call the required 
# function as a method on super():

class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound
 
  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))
 
class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 
 
pet_cat = Cat("Rachel")
pet_cat.make_noise() #Prints: Rachel says, Meow!

#######################################################
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()
    
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id() #Prints: My id is 3. I am an admin.