# Python-Text-Adventure-Engine
A Text Adventure Game Engine in Python.


Installation Instructions:
    1. Extract Player.py, game.py, and level.py into the same directory.
    2. run 'python game.py'
    3. Enjoy the demo!

I created this mainly as an exercise in game engine design. Games can be designed in the Level.py file. Room Dictionary Structure is as follows:

Rooms
     Room One
        Description (string)
        
        Items (Dictionary)
        
            Items.'item_one' (Dictionary)
        
                Items.'item_one'.'Description':'string description'
        
                Items.'item_one'.'damage':integer (Completely optional)
        
        Enemies (Ditionary, Optional)
        
            Enemies.'enemy_one' (Dictionary)
        
                Enemies.'enemy_one'.'hitpoints':integer
        
                Enemies.'enemy_one'.'power':integer
        
                Enemies.'enemy_one'.'Description':'String description'
        
        Exits (Dictionary)
        
            'Direction':'String Title of Room'
Any level can be added in the same format. The Items have an optional Damage - this is to track potential Weapons. 
The Combat system is entirely optional - if you do not wish to have a combat system, don't add any Enemies, and don't include the Items' damage. 

In short, feel free to branch this out and experiment with it. Thanks for looking!
