cars=100
space_in_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_car
average_person_per_car=passengers/cars_driven


print "There are",cars,"Cars","cars available"
print"There are only",drivers,"Drivers available"
print"There will be",cars_not_driven,"Empty cars today"
print"we can transport",carpool_capacity,"people today"
print"we have",passengers,"passengers"
print"we need to put about",average_person_per_car,"in each car"
