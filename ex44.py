class parent(object):
    def implicit(self):
        print"PAARENT implicit()"
    def override(self):
        print"This is parent and this might be overridden"
    def altered(self):
        print"Parent altered"
    
        
class child(parent):
    def override(self):
        print"This is child and its fucking overriding"
        
    def altered(self):
        print"Child alterred"
        super(child,self).altered()
        print"Chid after parent is altered"
    
dad=parent()
son=child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
