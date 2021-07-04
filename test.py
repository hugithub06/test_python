# import the pygame module, so you can use it
import pygame
import math
import random

def dessine_branche(screen, x, y, longeur, angle):
    newx = x+longeur*math.cos(math.radians(angle))
    newy = y-longeur*math.sin(math.radians(angle))
    pygame.draw.line(screen, (80, 50, 10), [x, y], [newx, newy], int(longeur/10))
    if longeur > 20:
        nb_branche = random.randint(2, 4)
        for x in range(0,nb_branche+1):
            new_longeur = int(longeur*random.randint(50, 70)*0.01)
            new_angle = angle + ((x-nb_branche*0.5) * 100 / nb_branche) + random.randint(-10, 10)
            dessine_branche(screen, newx, newy, new_longeur, new_angle)
    else :
        pygame.draw.circle(screen, (0, 255, 0), [newx, newy], 10)
            
    
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1650,1000))
    screen.fill((0, 90, 0))

    #load and set the logo
    logo = pygame.image.load("logo.png").convert_alpha()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    # define a variable to control the main loop
    running = True

    clock = pygame.time.Clock()
     
    while running:
        clock.tick(10)
        # Arthur test
        #screen.blit(logo, (10,10))
        dessine_branche(screen, 825, 900, 300, 90)
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
                pygame.quit()
        pygame.display.flip()
        running = False 
    #pygame.quit() 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
