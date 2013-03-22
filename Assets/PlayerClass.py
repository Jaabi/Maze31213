'''
Created on Mar 21, 2013

Player class. Not much else to be said

@author: Abdiel "Jaabi" Rodriguez
'''

import pygame

class Player(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Player_Standing-Down.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        #For now, place the player in the center of the screen
        self.rect.center = (320, 240)
    
    def update(self):
        pass
        