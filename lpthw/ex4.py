# create a variables and give them a value
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# calculate the number of cars that won't have drivers
cars_not_driven = cars - drivers
# create a variable for the number of cars driven; could also just use drivers but that wouldn't be as easy to read
cars_driven = drivers
# calculate how many how many people can fit in all the cars
carpool_capacity = cars_driven * space_in_a_car
# calculate how many passengers each car with a driver can hold
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."