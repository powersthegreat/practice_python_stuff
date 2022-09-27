# To implement this behavior, we must first discuss 
# dunder methods. Every defined class in Python has 
# access to a group of these special methods. We've 
# explored a few already, the constructor __init__() 
# and the string representation method __repr__(). 
# The name dunder method is derived from the Double 
# UNDERscores that surround the name of each method.
class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"

##################################################

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
  
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 + e1
m1 + e2
m1 + e3
print(len(m1))

