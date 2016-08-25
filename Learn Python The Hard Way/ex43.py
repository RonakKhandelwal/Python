from sys import exit
from random import randint



class Scene(object):
    def enter(self):
        print"This scene is not yet implimented subclass it and handle it enter()"
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map
    def play(self):
        current_scene=self.scene_map.opening_scene()
        
        while True:
            print "\n--------"
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)
            
        
class Death(Scene):

    quips=[
        "You died ,you kindof suck at it",
        "Your mom would be proud.......if you were just smarter",
        "such a luser",
        "I have a small puppy who's better than this"
        ]
    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print"The gothons of planet percal #25 have invaded your ship and destroyed"
        print"your entire crew. You are the last surviving member and your last"
        print"mission is to get the neutron destruct bomb from weapon armory"
        print"put it in the bridge and blow the ship up after getting into an"
        print"escape pod"
        print "\n"
        print"You're running down the central corridor to the metal armory when"
        print"a gothon jumps out ,red skin,dark teeth and a scary clown costumn"
        print"flowing around his hate filled body .he's blocking the door to the armory"
        print"and about to pull a weapon to blast you"
        
        action =raw_input("> ")
        
        if action=='shoot':
            print"quick on the draw you yank your blaster and fir at the goton"
            print"his clown costumn is flowing and moving around his body ,which throws"
            print"you off the aim and your laser hits the costumn but misses him entirly"
            print"completely ruin his brand new costumn which his mother bought him"
            print"makes him fly into rage and blast you repetedly in your face until you are dead and then he eats you"
            return 'death'
            
        elif action=='dodge':
            print"like a world class boxer you dodge ,slip sleave and slide right"
            print"as the goton blaster cranks a laser past your head"
            print"in the middle of the artful dodge your foot slips and"
            print"bang your head on the metal wall and you pass out"
            print"yo wake up shortly after to be eathon by goton stmps"
            return 'death'
        elif action=='tell a joke':
            print"Lucky for you they made you learn gothon insults in acadmy"
            print"you tell the one gothon joke you know"
            print"fvndfkjvnevj nfSKJFNKSVBB VJVN JVWKV JCK VKJVSV  kfv hbj KJDFKJVNK ,ANKJ "
            print"The gothon stops,tries not to laugh and then busts out laughting and can't move"
            print"while he's laughting you run up and shoot him square in the head"
            print"putting him down and then jump to the weapon armory door"
            
            return 'laser_weapon_armory'
        else:
            print"DOES NOT COMPUTE"
            return 'central_corridor'
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print"You dive and roll into the armory and scan the room"
        print"for more gotohns may be hiding .Its quite,dead quite"
        print"You stand up and run to the far side of the room"
        print"neutron bomb in the container .There's a keypad lock in the box"
        print"and you need the code to get the bomb out.If you get the code"
        print"wrong 10 times then the lock screen freezes forever and you can't"
        print"get the bomb the code is 3 digits"
        code='%d%d%d'%(randint(1,9),randint(1,9),randint(1,9))
        guess=raw_input("[KeyPad] > ")
        guesses=0
        
        while guess !=code and guesses<10:
            print"BZZZZDDDD"
            print"wrong code try again"
            guesses+=1
            guess=raw_input("[KeyPad] > ")
            
        if guess==code:
            print"The container opens and the gas comes out"
            print"You grab the neutron bomb and run as fast as you can to the"
            print"Bridge where you must place the bomb"
            return 'the_bridge'
        else:
            print"The lock buzzes one last time and you hear a sickning"
            print"melting sound as the mechanism is fused together"
            print"You decide to sit there and finally the gothon blow up the"
            print"ship from there ship and you die"
            return'death'

        
class TheBridge(Scene):
    
    def enter(self):
        print"You burst onto the bridge with the neutron destruct bomb"
        print"under your arms and surprise 5 gothons who are trying to"
        print"Take control of the ship. Each of then has an even uglier "
        print"clown costumn than the last.They haven't pulled their "
        print"weapons out yet as they see the bomb with you "
        print"And they don't wanna set it off"
        
        action=raw_input('> ')
        
        if action=="Throw the bomb":
            print"In panic you throw the bomb at the group of gothons"
            print"and make a ;eap to the door right as you drop it"
            print"a gothon shoots you right at the back killing you"
            print"As you die you see a gothon fanatically try to disarm "
            print"the bomb.You die knowing that they will probably blow up when it goes off"
            return'death'
        
        elif action=="slowly place the bomb":
            print"You point your blaster at the bomb in your arm"
            print"and the gothons put thier hands up and start to sweat"
            print"You inch backward to the door ,open it and then carefully"
            print"p;ace the bomb on the floor pointing at it"
            print"you then jump back out of the door and push the close button"
            print"and blast the lock so gothons can't go out"
            print"Now the bomb is placed you run to the escape pod"
            print"get off this tin can"
            return'escape_pod'
            
        else:
            print"DOES NOT COMPUTE"
            return'the_bridge'
            


class EscapePod(Scene):
    

    def enter(self):
        print"Some stuff.....bleh bleh bleh bleh and some random stuff"
        good_pod=randint(1,5)
        guess=raw_input('[POD#]=')
        
        if int(guess)!=good_pod:
            print"You get into %d pod"%guess
            return 'death'
        
        else:
            print"HBHABHDBHXKJNDAK  JDJB JDBJ"
            return 'finished'
        
    
        
    
        

class Map(object):
    
    scenes={
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory':LaserWeaponArmory(),
        'the_bridge':TheBridge(),
        'escape_pod':EscapePod(),
        'death':Death()
        
    }
    def __init__(self,start_scene) :
        self.start_scene=start_scene
        
            
    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)
            
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
   
a_map=Map('central_corridor')     
a_game=Engine(a_map)
a_game.play()
        
        

