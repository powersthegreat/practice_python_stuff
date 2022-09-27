# Let’s now look at a feature allowed by Python called multiple
# inheritance. As you may have guessed from the name, this is 
# when a subclass inherits from more than one superclass. One form 
# of multiple inheritance is when there are multiple levels of 
# inheritance. This means a class inherits members from its 
# superclass and its super-superclass.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))
 
class Cat(Animal):
  pass
 
class Angry_Cat(Cat):
  pass
 
my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() #Prints: Mr. Cranky says, Hi!

####################################################
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

# Write your code below
class Manager(Admin):
  def say_id(self):
    print("I am in charge.")
    super().say_id()


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e4.say_id() #Prints: I am in chage. My id is 4. I am an admin.

