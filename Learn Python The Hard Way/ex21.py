def add(a,b):
    print "Adding %d to %d"%(a,b)
    return a+b

def subtract(a,b):
    print "Subtracting %d from %d"%(a,b)
    return b-a

def multiply(a,b):
    print "Multiplying %d and %d"%(a,b)
    return a*b

def devide(a,b):
    print "Deviding %d from %d"%(a,b)
    return a/b

print "Lets do some math functions"    

age=add(30,5)
height=subtract(78,4)
weight=multiply(45,2)
iq=devide(100,2)

print "Age:%d Height:%d Weight:%d Iq:%d"%(age,height,weight,iq)

print"Here's a puzzle"

what=add(age,subtract(height,multiply(weight,devide(iq,2))))

print "That becomes",what,"Can you do it by hand???"
#learn difffrent printing techniques!!!!
