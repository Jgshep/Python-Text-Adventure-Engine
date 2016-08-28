import Player
import level

Person=Player.Player('Hallway')


quit = False
prompt = '> '
level.Describe(Person)

hallDoorLocked = True

while quit != True:
 ## 
    print 'Now what?'
    command = raw_input(prompt)
    lower=command.lower()
    if 'look' in lower:
        Player.Look(Person)
    ###MOVE#####
    elif 'move' in lower:
        processed = lower.split()
        if processed[1] in level.Rooms[Person.curPosition]['Exits']:
            if Person.curPosition == 'Hallway' and level.Rooms[Person.curPosition]['Exits'][processed[1]]=='Courtyard':
                if 'key' not in Person.inventoryItems and hallDoorLocked == True:
                    print 'The door is locked, and you do not have a key.'
                   

                elif 'key' in Person.inventoryItems and hallDoorLocked == True:
                    print 'You unlock the door with your key and step through.'
                    hallDoorLocked = False
                    level.Move(Person, processed[1])
                else:
                    level.Move(Person, processed[1])
                 
            else:
                level.Move(Person, processed[1])


        elif processed[1] not in level.Rooms[Person.curPosition]['Exits']:
            print 'Not a valid exit. Please try again.'
        else:
            print 'Move Input not understood. Please try again.' 
    ###ENDMOVE###
    ###ATTACK###
    elif 'attack' in lower:
        processed = lower.split()
        try:
            if processed[1] in level.Rooms[Person.curPosition]['Enemies']:
                curEnemy = processed[1]
                print 'You have %d HP. The %s has %d HP.' % (Person.hitpoints, curEnemy, level.Rooms[Person.curPosition]['Enemies'][curEnemy]['hitpoints'])
                Player.Attack(Person, curEnemy)
            elif processed[1] not in level.Rooms[Person.curPosition]['Enemies']:
                print 'That enemy is not here.'
            else:
                print 'Input not understood. Please try again.'
        except (IndexError, KeyError):
            print 'You haven\'t given me an enemy to attack! Please try again.'
    
    ###ENDATTACK###

    ##EQUIP##
    elif 'equip' in lower:
        processed = lower.split()
        if processed[1] in Person.inventoryItems:
            weapon = processed[1]
        if processed[0] == 'equip':
                Player.Equip(Person, weapon)

        elif processed[0] == 'unequip':
            Player.Unequip(Person, weapon)
        else:
            print 'The %s is not in your inventory.' %processed[1]
    ##END EQUIP##


    elif 'quit' in lower or 'exit' in lower:
        quit = True

    elif 'inventory' in lower:
        Player.Inventory(Person)

    elif 'pickup' in lower:
        processed=lower.split()
        if processed[1] in level.Rooms[Person.curPosition]['Items']:
            Person.inventoryItems[processed[1]]=level.Rooms[Person.curPosition]['Items'][processed[1]]
            del level.Rooms[Person.curPosition]['Items'][processed[1]]
            print 'You picked up the %s.' %processed[1]
        else: print 'That item is not in this room.'

    else:
        print 'Command not understood. Please try again.'

