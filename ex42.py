## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name
		print "This ia a Dog is-a Animal has a name %s" % self.name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		print "This ia a Cat is-a Animal has a name %s" % self.name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name
		self.name = name
		print "This ia a Person has a name %s" % self.name

		## Person has-a pet of some kind
		self.pet = None
		print "This Person has a pet %s" % self.pet

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? HOW TO USE super??
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		print "This is a Employee has a salary %s" % self.salary

## Fish is-a object
class Fish(object):
	## ?? USE WHICH ARGUMENTS  
	def sayName(self):
		print "This is-a fish!"

## Salmon is-a Fish
class Salmon(Fish):
	
	def sayName(self):
		print "This is-a Salmon!"

## Halibut is-a Fish
class Halibut(Fish):
	
	def sayName(self):
		print "This is-a Halibut!"


## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet is-a satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet is-a rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()
flipper.sayName()

## crouse is-a Salmon
crouse = Salmon()
crouse.sayName()

## harry is-a Halibut
harry = Halibut()
harry.sayName()