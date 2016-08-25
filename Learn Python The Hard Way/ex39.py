#create a mapping of states to abbreviations

states ={
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}


cities ={
    'CA':'San Fransisco',
    'MI':'Deteroit',
    'FL':'Jacksonville'
}

cities['NY']='New York'
cities['OR']='Portland'

print'-'*10
print"NY state has city ",cities['NY']
print"OR state ha city ",cities['OR']

print'-'*10
print"Michigan abbreviation is ",states['Michigan']
print"Florida abbreviation is ",states['Florida']

print '-'*10
print"Michigan has :",cities[states['Michigan']]
print"Florida has :",cities[states['Florida']]

print'-'*10
for state,abbrev in states.items():
    print"%s is abbreviated as %s"%(state,abbrev)

print'-'*10
for abbrev,city in cities .items():
    print"%s has the city %s"%(abbrev,city)
    
print'-'*10
for state,abbrev in states.items():
    print"%s is abbreviated as %s and has the city %s"%(state,abbrev,cities[abbrev])
    
print'-'*10
state=states.get('Texas',None)

if not state:
    print"Sorry,No Texas"
    
city=cities.get('TX',"Does not exists")
print "The City of state TX is : %s "%city

