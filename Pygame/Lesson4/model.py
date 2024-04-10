#!/usr/bin/env python3
################# SUPRESS PYGAME SUPPORT MESSAGE ###################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
####################################################################

# Import our modules
import pygame, time
import sprites, enemies

class Model():
    def __init__(self):
        self.worldMap = {"ENVIRONMENT": []}
        # Load map
        self.mapLoad()

        # Drop Clyde into our world
        self.clyde = sprites.Clyde(100, 100)
        self.slime = enemies.Slime(300, 300)
        pass

    def update(self):
        # Update our world
        self.slime.update()
        self.clyde.update()
        pass

    def mapLoad(self):
        # Load the map
        fyle = open('map.txt', mode='r')
        
        try:
            self.map = eval(fyle.read())
        except:
            self.map = None
        
        fyle.close()

        # Now we try to place all the objects in our map
        count = 0
        for key, value in self.map.items():
            print("Loading: " + key)
            if (key == "ENVIRONMENT"):
                for secondKey, secondValue in value.items():
                    print(secondKey, secondValue)
                    envObj = getattr(sprites, secondValue[0])
                    envObj = envObj(secondValue[1][0], secondValue[1][1])
                    #envOvj = envObj(secondValue[1][0], secondValue[1][1])
                    self.worldMap["ENVIRONMENT"].append(envObj)
                    count += 1
    
    def mapSave(self):
        # Save the map
        fyle = open('map.txt', mode='w')
        fyle.write(self.map)
        fyle.close()
