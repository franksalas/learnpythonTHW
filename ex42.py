## Animal is-a object
class Animal(object): pass


# is-a Animal. Dog class is-a Animal
class Dog(Animal):  # class Dog has-a init that takes self, name as parameters
    def __init__(self, name):
        # has-a name. Dog class has-a name.
        self.name = name  # from self get name attribute and set it to name


# is-a Animal
class Cat(Animal):  # class cat has a init with self and name as parameters
    def __init__(self, name):
        # has-a name. Cat class has a name
        self.name = name  # from self get name attribute and set it to name


# is-a object , Person
class Person(object):  # class person has-a init that takes self and name as parameters.
    def __init__(self, name):
        # has-a name. Person class has-a name
        self.name = name  # from self take name attribute and set it to name

        # Person has-a pet of some kind
        self.pet = None  # form self take the pet attribute and set it to None


# is-a. Emplpyee class is-a object.
class Employee(Person):  # class employee has-a init that takes self, name salary as parameters.
    def __init__(self, name, salary):
        # ? wha tis this strange maginc?
        super(Employee, self).__init__(name)
        #  has-a. Employee has a salary.
        self.salary = salary


# is-a. Fish is-a object
class Fish(object): pass


# is-a. Salmon is-a Fish
class Salmon(Fish): pass


# is-a. Halibut is-a Fish
class Halibut(Fish): pass


# rover is-a Dog
rover = Dog("Rover")  # set rover to an instance of class Dog with "Rover" as parameters

# sam is-a Cat
sam = Cat("Sam")  # set sam to an instance of the class Cat with "Sam" as patameres

# mary is-a Person
mary = Person("Mary")

# sam is-a pet
mary.pet = sam # from mary get the pet attribute and set it to the instance sam

# frak is-a employee
frank = Employee("Frank", 120000)


# rover isa pet
frank.pet = rover  # from frank get the pet attribute and set it to the instance rover

#
flipper = Fish()


# ?
crouse = Salmon()


# ?
harry = Halibut()


