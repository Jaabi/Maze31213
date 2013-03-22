'''
Created on Mar 18, 2013

Real project was created on Mar 12, 2013

First REAL start on the Maze 31213 project. Hear wee goe!

Follows the example of the IDEA/ALTER game framework by Andy Harris in the book "Game Programming: The L Line, The Express Line to Learning", published by Wiley Publishing, Inc.


@author: Abdiel "Jaabi" Rodriguez
'''

#HAHAHAHAHAHAHAHAHAHAHAHAHAHA I FINALLY GOT THIS TO WORK CORRECTLY! YEYEYEYEYEYEYEYEYEYEYEYEYEY~~~~~~~~~!@!!!!!!!!!!!!!!
        
#I - Import and Initialize
import pygame, BgAndTxtClasses, PlayerClass
pygame.init()


#Not to be called more than once unless you know what you're doing
def main():
    
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Maze 31213")
    
    #E - Entities (all sprites will be in their respective modules, 
        # being brought in through imports)
        
        #Getting ready for a fully-implemented BackgroundSprite class
    bgSprite = BgAndTxtClasses.BackgroundSprite()
        #Will move these objects to a CONTROL object that will be responsible
        # for all interactions, except for some specific things
    player = PlayerClass.Player()
    
    allSprites = pygame.sprite.OrderedUpdates(bgSprite, player)
    
    #A - Action (broken into ALTER steps)
    
        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
        
        #L - Set up main loop
    while keepGoing:
        #T - Timer to set frame rate
        clock.tick(30)
        
        #E - Event handlint
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        #R - Refresh display
        
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

    #All sprites are now being destroyed or have already been destroyed. Yay~


if __name__ == '__main__':
    main()
