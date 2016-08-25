ten_things="Apples oranges crows telephone light sugar"

print"Wait there are not 10 thing in that list lets fix that"

stuff=ten_things.split(" ")
more_stuff=["Day","night","song","frisbee","corn","banana","girl","boy"]
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "Adding: " ,next_one
    stuff.append(next_one)  
    print"There are %d items right now"%len(stuff)

print"There we go,",stuff

print"Lets do something with stuff"

print stuff[1]
print stuff[-1]#whoa!! fancy
print stuff.pop()
print"".join(stuff)
print"#".join(stuff[3:5])


