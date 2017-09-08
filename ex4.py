# the number of cars
cars = 100
# the sapce of a car
space_in_a_car = 4
# the number of drivers
drivers = 30
# the number of passengers
passengers = 90
# the number of cars not in use
cars_not_driven = cars - drivers
# the number of cars in use
cars_driven =drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car." 