## Program to illustrate public access modifier in a class
class Geek:
    # Constructor
    def __init__(self, name, age):
        # Public data members
        self.geekName = name
        self.geekAge = age

    # Public member function
    def displayAge(self):
        # Accessing public data member
        print("Age: ", self.geekAge)

# Creating object of the class
obj = Geek("R2J", 20)

# Accessing public data member
print("Name: ", obj.geekName)

# Calling public member function of the class
obj.displayAge()

# Program to illustrate protected access modifier in a class

class Student:  # Superclass
    # Protected data members
    _name = None
    _roll = None
    _branch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # Protected member function
    def _displayRollAndBranch(self):
        # Accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

class Geek(Student):  # Derived class
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # Public member function
    def displayDetails(self):
        # Accessing protected data members of superclass
        print("Name: ", self._name)
        # Accessing protected member functions of superclass
        self._displayRollAndBranch()

# Creating an object of the Geek class
obj = Geek("R2J", 1706256, "Information Technology")

# Calling public member function of the class
obj.displayDetails()

# Program to illustrate private access modifier in a class

class Geek:
    # Private members
    __name = None
    __roll = None
    __branch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # Private member function
    def __displayDetails(self):
        # Accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    # Public member function
    def accessPrivateFunction(self):
        # Accessing private member function
        self.__displayDetails()

# Creating object of the class
obj = Geek("R2J", 1706256, "Information Technology")

# Calling public member function of the class
obj.accessPrivateFunction()

# Program to illustrate access modifiers of a class

class Super:  # Super class
    # Public data member
    var1 = None
    # Protected data member
    _var2 = None
    # Private data member
    __var3 = None

    # Constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # Public member function
    def displayPublicMembers(self):
        # Accessing public data members
        print("Public Data Member: ", self.var1)

    # Protected member function
    def _displayProtectedMembers(self):
        # Accessing protected data members
        print("Protected Data Member: ", self._var2)

    # Private member function
    def __displayPrivateMembers(self):
        # Accessing private data members
        print("Private Data Member: ", self.__var3)

    # Public member function to access private members
    def accessPrivateMembers(self):
        # Accessing private member function
        self.__displayPrivateMembers()

# Creating object of the class
obj = Super("Public Value", "Protected Value", "Private Value")

# Calling public member function
obj.displayPublicMembers()

# Calling protected member function (direct access from outside is not recommended)
obj._displayProtectedMembers()

# Calling public member function to access private data
obj.accessPrivateMembers()

# Base class (Super class)
class Super:
    # Public data member
    var1 = None
    # Protected data member
    _var2 = None
    # Private data member
    __var3 = None

    # Constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # Public member function
    def displayPublicMembers(self):
        # Accessing public data members
        print("Public Data Member: ", self.var1)

    # Protected member function
    def _displayProtectedMembers(self):
        # Accessing protected data members
        print("Protected Data Member: ", self._var2)

    # Private member function
    def __displayPrivateMembers(self):
        # Accessing private data members
        print("Private Data Member: ", self.__var3)

    # Public member function to access private members
    def accessPrivateMembers(self):
        # Accessing private member function
        self.__displayPrivateMembers()


# Derived class (Sub class)
class Sub(Super):
    # Constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # Public member function to access protected members
    def accessProtectedMembers(self):
        # Accessing protected member functions of the super class
        self._displayProtectedMembers()


# Creating objects of the derived class
obj = Sub("Geeks", 4, "Geeks !")

# Calling public member functions of the class
obj.displayPublicMembers()  # Accesses public member from Super class
obj.accessProtectedMembers()  # Accesses protected member from Super class
obj.accessPrivateMembers()  # Accesses private member function from Super class

# Object can access protected member
print("Object is accessing protected member:", obj._var2)

# Object cannot access private member, so it will generate AttributeError
# Uncommenting the line below will result in an error
# print(obj.__var3)  # Will raise an AttributeError