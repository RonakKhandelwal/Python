## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
    
## is-a
class dog(Animal):
    
    def __init__(self,name):
       ##has-a
        self.name=name
        
## is-a
class cat(Animal):
    def __init__(self,name):
        ## has-a
        self.name=name
    
##is-a 
class person(object):
    def __init__(self,name):
        self.name=name
        self.pet=None
        
class employee(person):
    def __init__(self,name,salary):
        super(employee,self).__init__(name)
        self.salary=salary

class Fish(object):
    pass
    
class Salmon(Fish):
    pass
    
class Halibut(Fish):
    pass

rover=dog("Rover")

satan=cat("Satan")

mary=person("mary")

mary.pet=satan

frank=employee("Frank",1200000)

frank.pet=rover


flipper=Fish()

crouse=Salmon()

harry=Halibut()
        
