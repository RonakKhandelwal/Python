from sys import exit

def gold_room():
    print"This room is full of gold so what do we take"
    next=raw_input("> ")
    if "0" in next or "1" in next:
        how_much=int(next)
        
    else:
        dead("Man,learn to type a number")
        
    if how_much<50:
        print"Nice ,Not greedy,you win"
        exit(0)
        
    else:
        dead("You greedy bastard!!")

def bear_room():
    print"The bear is here"
    print"The bear has a bunch of honey"
    print"The fat bear is in front of another door"
    print"How are you gonna move the bear"
    bear_moved=False
    
    while True:
        next=raw_input("> ")
        
        if next=="take honey":
            dead("THE bear slaps your face off")
            
        elif next=="taunt bear" and not bear_moved:
            print"The bear has moved from the door"
            bear_moved=True
            
        elif next=="taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
            
        elif next=="Open door" and bear_moved:
            gold_room()
            
        else:
            print"I got no idea what that means"
            
def cthulhu_room():
    print"Here you see the evil cthulhu"
    print"he,it,whenever stares at you you go crazy"
    print"Do you flee for your life or eat your head"
    
    next=raw_input("> ")
    
    if "flee" in next:
        start()
        
    elif "eat" in next:
        dead("well that was tasty")
        
    else:
        cthulhu_room()
        

def dead(why):
    print why,"Good job"
    exit(0)   

def start():
    print"You ar in a dark room"
    print"One door to your right and on to left,which one ould you take"
    next=raw_input("> ")
    
    if next=="left":
        bear_room()
        
    elif next=="right":
        cthulhu_room()
        
    else:
        dead("You stumble around the room until you starve")

start()
        
    
