# As we can see, there are some clear advantages of 
# utilizing inheritance. Not only are we able to reuse 
# methods across multiple classes using our parent 
# class, but we are also able to create parent-child 
# relationships between entities!

#Parent Class
class Animal: 
  def eat(self): 
    print("Nom Nom Nom...eating food!")

#Child Class
class Dog(Animal):
  def bark(self):
    print('Bark!')
#Child Class
class Cat(Animal):
  def meow(self):
    print('Meow!')

fluffy = Dog()
zoomie = Cat()
 
fluffy.eat() #Prints: Nom Nom Nom...eating food!
zoomie.eat() #Prints: Nom Nom Nom...eating food!


####################################################
#Parent Class
class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

#Child Class
class Admin(Employee):
  pass


e1 = Employee()
e2 = Employee()
e3 = Admin()

e1.say_id() #Prints: My id is 1.
e2.say_id() #Prints: My id is 2.
e3.say_id() #Prints: My id is 3.