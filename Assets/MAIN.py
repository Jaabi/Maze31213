'''
Created on Mar 18, 2013

Real project was created on Mar 12, 2013

First REAL start on the Maze 31213 project. Hear wee goe!

Follows the example of the IDEA/ALTER game framework by Andy Harris in the book "Game Programming: The L Line, The Express Line to Learning", published by Wiley Publishing, Inc.


@author: Abdiel "Jaabi" Rodriguez
'''

#HAHAHAHAHAHAHAHAHAHAHAHAHAHA I FINALLY GOT THIS TO WORK CORRECTLY! YEYEYEYEYEYEYEYEYEYEYEYEYEY~~~~~~~~~!@!!!!!!!!!!!!!!
        
#I - Import and Initialize
import pygame, BgAndTxtClasses
pygame.init()


#Not to be called more than once unless you know what you're doing
def main():
    
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Maze 31213")
    
    #E - Entities
        #All the sprites, but I think they'll go in their own module
        #background for now
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 255, 255))
        #Getting ready for a fully-implemented BackgroundSprite class
    bgSprite = BgAndTxtClasses.BackgroundSprite
    
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
        #This is needed for now, but it will be unnecessary once a sprite is implemented for the background
        screen.blit(background, (0, 0))
        pygame.display.flip()

    #All sprites are now being destroyed or have already been destroyed. Yay~


if __name__ == '__main__':
    main()
