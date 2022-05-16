import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

""" 
Recursive rectangle function.  
use following method to draw a rectangle on the screen:
pygame.draw.rect(screen, BLACK, [x, y, width, height],1)
"""
def recursive_draw(x, y, width, height, screen):
    if width <= 10 or height <= 10:
        return "Too small"
    pygame.draw.rect(screen, BLACK, [x, y, width, height], 1)

    x = x + width * 0.1
    y = y + height * 0.1
    width = width * 0.8
    height = height * 0.8

    recursive_draw(x, y, width,height, screen)

""" main function that will be executed """
def main(): 
    # Init 
    running = True
    width, height = 700, 700
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        screen.fill(WHITE)
    
        """ Should draw rectangles as indicated in GitHub """
        recursive_draw(0, 0, width, height, screen)
    
        pygame.display.flip()
        clock.tick(60)
    
    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()