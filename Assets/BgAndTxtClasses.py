'''
Created on Mar 20, 2013

Background class and all classes that have to do with showing text on the screen

@author: Abdiel "Jaabi" Rodriguez
'''
import pygame

class BackgroundSprite(pygame.sprite.Sprite):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\Background.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        #Ensure that the background gets fully shown
        self.rect.topleft = (0,0)
    
    def update(self):
        pass

#To be finished at a later date
#class Text(pygame.sprite.Sprite):
#    '''
#    classdocs
#    '''
#
#    def __init__(self):
#        '''
#        Constructor
#        '''
#        pygame.sprite.Sprite.__init__(self)
        
