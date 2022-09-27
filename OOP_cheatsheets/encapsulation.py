# Encapsulation is the process of making methods 
# and data hidden inside the object they relate to. 
# Languages accomplish this with what are called 
# access modifiers like:

# -Public
# -Protected
# -Private

# In general, public members can be accessed from 
# anywhere, protected members can only be accessed 
# from code within the same module and private 
# members can only be accessed from code within 
# the class that these members are defined.

class Employee():
    def __init__(self):
        self.id = None
        self._id = None
        self.__id = None
        # Write your code below
        

e = Employee()
print(dir(e))