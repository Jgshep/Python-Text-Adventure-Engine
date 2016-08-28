import Player
print 'This is a level test. Time to combine this stuff.'

###ROOMS####
Rooms={}
Rooms['Kitchen']={}
Rooms['Kitchen']['Description']='a place for cooking'

Rooms['Kitchen']['Items']={}
Rooms['Kitchen']['Items'][ 'cheese']={
    'Description':'a block of semihard, white cheese'
}
Rooms['Kitchen']['Items']['knife']={
    'damage':1,
    'Description':'a sharp stabby thing'
}

##Kitchen exits
Rooms['Kitchen']['Exits']={
    'north':'Bedroom',
    'west':'Hallway'
}
##end Kitchen

##Begin Bedroom

Rooms['Bedroom']={}
Rooms['Bedroom']['Description']='a place for sleeping'


Rooms['Bedroom']['Items']={}
Rooms['Bedroom']['Items']['suit']={
        'Description':'a fancy set of clothes'
}
Rooms['Bedroom']['Items']['comb'] = {
        'Description':'to fix your unruly hair'
}
Rooms['Bedroom']['Items']['key']={
    'Description':'to unlock things'
}
##Bedroom Exits
Rooms['Bedroom']['Exits']={
        'south':'Kitchen'
    }

##End Bedroom

##Begin Hallway
Rooms['Hallway']={}
Rooms['Hallway']['Description']='the entrance to this home'
Rooms['Hallway']['Items']={}
Rooms['Hallway']['Items']['umbrella']={
    'Description':'for a rainy day'
}
Rooms['Hallway']['Items']['shoes'] = {
      'Description':'for walking'
}

Rooms['Hallway']['Exits']={
        'east':'Kitchen',
        'south':'Courtyard'
    }


##End Hallway

##Begin Courtyard

Rooms['Courtyard']={}
Rooms['Courtyard']['Description']='a lovely front yard, with a flower garden and benches.'

Rooms['Courtyard']['Enemies']={}
Rooms['Courtyard']['Enemies']['cockroach']={
        'hitpoints':2,
        'power':1,
        'Description':'a gigantic roach, hellbent on destroying you.'
}

Rooms['Courtyard']['Exits']={
        'north':'Hallway',
        'west':'Drawbridge'
    }
##End Courtyard

##Begin Drawbridge
Rooms['Drawbridge']={}
Rooms['Drawbridge']['Description']='a rickety-looking rope bridge over a gaping chasm.'
Rooms['Drawbridge']['Enemies']={}
Rooms['Drawbridge']['Enemies']['goblin']={
        'hitpoints':5,
        'power':1,
        'Description':'a feeble goblin guarding the drawbridge!'
    }
Rooms['Drawbridge']['Exits']={
        'east':'Courtyard'
    }
##ToDo: Add enemies. First I have to make a combat system.
##End Drawbridge

###END ROOMS

###BEGIN PLAYER###

def Describe(Person):
    print '\n\n'
    print '+'*50
    print '\n'
    print 'You are in the %s, %s' % (Person.curPosition, Rooms[Person.curPosition]['Description'])
    try:
        print 'The items contained within are: '
        for item in Rooms[Person.curPosition]['Items'].items():
            item_dict=dict(item[1])
            print '\t* %s, %s' %(item[0], item_dict['Description'])
            try:
                print '\t Damage: %d' % item_dict['damage']
            except KeyError:
                pass

#            print '\t* %s, %s' %(item, description)
    except KeyError:
        print '\t<no items>'
    
    try:
        for enemy in Rooms[Person.curPosition]['Enemies'].iteritems():
            enemy_dict=dict(enemy[1])
            print 'A foe is here! The %s, %s' %(enemy[0], enemy_dict['Description'])
            print 'It has %d hitpoints and %d power.' %(enemy_dict['hitpoints'], enemy_dict['power'])
                

    except KeyError:
        pass
    print 'The exits are to the: '
    for exit, location in Rooms[Person.curPosition]['Exits'].items():
        print '\t - %s, the %s' %(exit, location)
    print '+'*50

def Move(Person, place):
    Person.curPosition = Rooms[Person.curPosition]['Exits'][place]
    Describe(Person)


