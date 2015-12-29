class other(object):
    def implicit(self):
        print"PAARENT implicit()"
    def override(self):
        print"This is parent and this might be overridden"
    def altered(self):
        print"Parent altered"
        
class child(object):
    def __init__(self):
        self.other=other()
    def implicit(self):
        self.other.implicit()
    
son=child()
son.implicit()
