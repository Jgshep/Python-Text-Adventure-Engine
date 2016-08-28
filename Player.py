import level
import random

class Player:

    def __init__(self, position):
        self.curPosition=position
    inventoryItems={}
    hitpoints=10 #base - will eventually be able to change with experience system
    attackPwr=1 #again, base.
    equipped = ''
dead = False

def Move(direction):
    Player.curPosition=direction

def Look(person):
    level.Describe(person)



def Inventory(Person):
    print '-'*50
    print 'Your inventory contains the following: '
    for item in Player.inventoryItems.items():
        item_dict=dict(item[1])
        print '\t* %s, %s' % (item[0],item_dict['Description'])
    print 'You currently have %d hitpoints' %Person.hitpoints
    print 'Your current attack power is %d.' %Person.attackPwr
    if not Person.equipped:
        print 'You are currently weilding your two bare hands. Or more, if you\'re a multiply-appendeged individual.'
    else:
        print 'You are currently weilding %s.' %Person.equipped
    print '-'*50
    
####COMBAT############################################################
#I need: 
#       HP (can set in Player.__init__) done
#       base attack (1 - in init?)      done
#       attack subroutine
#       block subroutine?
#
#I'm going to need a random number generator. 
#I'll use the 1d2, 2d2 etc style 
#starting with 1d1, random values can be between 0 and 2
#Enemies will start with 1d1, with 5 HP.
#Functions:
#   Roll(damage) - random number generator, accepts damage variable
#       Attack() will probably get the damage variable from Player.attackPwr
#           Upon pickup, knife grants +1 to attackPwr? Sure, that's easy enough
#Could I use a class like Player() to create enemies? humm. 
#   I think using an 'Enemies' entry in the room's dictionary would be easier.
######################################################################

def Attack(Person, enemy):
    damage=Roll(Person.attackPwr)
    level.Rooms[Person.curPosition]['Enemies'][enemy]['hitpoints']-=damage
    if damage == Person.attackPwr:
        print 'Critical hit! You hit the %s for %d points of damage!' %(enemy, damage)
    elif damage == 0:
        print 'You hit the shadow of the %s. Unfortunately, the actual %s takes no damage.' %(enemy, enemy)
    else:
        print 'You strike at the %s for %d points of damage.' %(enemy, damage)
    if level.Rooms[Person.curPosition]['Enemies'][enemy]['hitpoints'] <= 0:
        print 'You have vanquished the %s!' %enemy
        del level.Rooms[Person.curPosition]['Enemies'][enemy]
    else:
        print 'The %s swings at you!' %enemy
        damage=Roll(level.Rooms[Person.curPosition]['Enemies'][enemy]['power'])
        if damage == 0:
            print 'You deftly sidestep the blow, taking 0 damage.'

        else:
            print 'The %s hits you for %d damage.' %(enemy, damage)

        Person.hitpoints -= damage
        if Person.hitpoints <= 0:
            print 'Oh no! You have died. Better luck next time!'
            dead = True
        else:
            print 'You have %d HP remaining. The %s has %d HP. ' %(Person.hitpoints, enemy, level.Rooms[Person.curPosition]['Enemies'][enemy]['hitpoints'])
def Roll(damage):
    #Will need to return a value.
    return random.randint(0,damage)

###############################
#Equip: Takes a Player instance variable, and an item (from levelTest.Rooms[room]['Items'][item])
#Checks the item's ['power'] (item will need to be expanded), and adds +(power) to Person.attackPwr
#Will also need an Unequip subroutine
#Checking to make sure it's a valid item will be done in gameTest, where this function is called.
###############################
def Equip(Person, item):
    try:
        print 'You attempt to equip the %s, %s.' %(item, Person.inventoryItems[item]['Description'])
        Person.attackPwr += (Person.inventoryItems[item]['damage'])
        Person.equipped=item
        print 'You feel stronger! Your attack has gone up by %d' %(Person.inventoryItems[item]['damage'])
    except KeyError:
        print '''That's not a weapon! Try again.'''


